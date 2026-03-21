#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT_DIR = Path(__file__).resolve().parents[1]
FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
REFERENCE_RE = re.compile(r"^\s{0,3}\[([^\]]+)\]:\s*(.+?)\s*$")
URI_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def normalize_reference_label(label: str) -> str:
    return " ".join(label.strip().lower().split())


def strip_fenced_code_blocks(text: str) -> str:
    output: list[str] = []
    in_fence = False
    fence_char = ""
    fence_len = 0

    for line in text.splitlines(keepends=True):
        if not in_fence:
            match = FENCE_RE.match(line)
            if match:
                marker = match.group(1)
                in_fence = True
                fence_char = marker[0]
                fence_len = len(marker)
                continue
            output.append(line)
            continue

        stripped = line.lstrip()
        if stripped.startswith(fence_char * fence_len):
            in_fence = False
            fence_char = ""
            fence_len = 0

    return "".join(output)


def parse_reference_destination(raw: str) -> str:
    raw = raw.strip()
    if not raw:
        return ""
    if raw.startswith("<"):
        end = raw.find(">")
        if end != -1:
            return raw[1:end].strip()
    return raw.split()[0].strip()


def parse_reference_definitions(text: str) -> dict[str, str]:
    definitions: dict[str, str] = {}
    for line in text.splitlines():
        match = REFERENCE_RE.match(line)
        if not match:
            continue
        label = normalize_reference_label(match.group(1))
        destination = parse_reference_destination(match.group(2))
        if destination:
            definitions[label] = destination
    return definitions


def read_bracket_content(text: str, start: int) -> tuple[int | None, str]:
    if start >= len(text) or text[start] != "[":
        return None, ""
    depth = 1
    cursor = start + 1
    while cursor < len(text):
        char = text[cursor]
        if char == "\\":
            cursor += 2
            continue
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                return cursor, text[start + 1 : cursor]
        cursor += 1
    return None, ""


def parse_optional_title_and_close(text: str, cursor: int) -> int | None:
    while cursor < len(text) and text[cursor].isspace():
        cursor += 1
    if cursor >= len(text):
        return None
    if text[cursor] == ")":
        return cursor + 1

    if text[cursor] in "\"'":
        quote = text[cursor]
        cursor += 1
        while cursor < len(text):
            if text[cursor] == "\\":
                cursor += 2
                continue
            if text[cursor] == quote:
                cursor += 1
                break
            cursor += 1
    elif text[cursor] == "(":
        depth = 1
        cursor += 1
        while cursor < len(text) and depth > 0:
            if text[cursor] == "\\":
                cursor += 2
                continue
            if text[cursor] == "(":
                depth += 1
            elif text[cursor] == ")":
                depth -= 1
            cursor += 1
    else:
        return None

    while cursor < len(text) and text[cursor].isspace():
        cursor += 1
    if cursor < len(text) and text[cursor] == ")":
        return cursor + 1
    return None


def parse_inline_destination(text: str, cursor: int) -> tuple[str | None, int | None]:
    while cursor < len(text) and text[cursor].isspace():
        cursor += 1
    if cursor >= len(text):
        return None, None

    if text[cursor] == "<":
        end = text.find(">", cursor + 1)
        if end == -1:
            return None, None
        destination = text[cursor + 1 : end].strip()
        close_index = parse_optional_title_and_close(text, end + 1)
        return destination, close_index

    start = cursor
    depth = 0
    while cursor < len(text):
        char = text[cursor]
        if char == "\\":
            cursor += 2
            continue
        if char == "(":
            depth += 1
            cursor += 1
            continue
        if char == ")":
            if depth == 0:
                break
            depth -= 1
            cursor += 1
            continue
        if char.isspace() and depth == 0:
            break
        cursor += 1

    destination = text[start:cursor].strip()
    close_index = parse_optional_title_and_close(text, cursor)
    return destination, close_index


def extract_links(text: str) -> tuple[list[tuple[str, str]], dict[str, str]]:
    body = strip_fenced_code_blocks(text)
    definitions = parse_reference_definitions(body)
    links: list[tuple[str, str]] = []

    cursor = 0
    while cursor < len(body):
        char = body[cursor]

        if char == "`":
            tick_count = 1
            while cursor + tick_count < len(body) and body[cursor + tick_count] == "`":
                tick_count += 1
            close = body.find("`" * tick_count, cursor + tick_count)
            if close == -1:
                break
            cursor = close + tick_count
            continue

        if char == "!" and cursor + 1 < len(body) and body[cursor + 1] == "[":
            cursor += 1
            char = "["

        if char != "[":
            cursor += 1
            continue

        label_end, label = read_bracket_content(body, cursor)
        if label_end is None:
            cursor += 1
            continue

        next_cursor = label_end + 1
        while next_cursor < len(body) and body[next_cursor].isspace():
            next_cursor += 1

        if next_cursor < len(body) and body[next_cursor] == "(":
            destination, close_index = parse_inline_destination(body, next_cursor + 1)
            if destination is not None and close_index is not None:
                links.append(("inline", destination))
                cursor = close_index
                continue

        if next_cursor < len(body) and body[next_cursor] == "[":
            ref_end, ref = read_bracket_content(body, next_cursor)
            if ref_end is not None:
                ref_label = ref if ref.strip() else label
                links.append(("reference", ref_label))
                cursor = ref_end + 1
                continue

        cursor = label_end + 1

    return links, definitions


def should_skip_destination(destination: str) -> bool:
    if not destination:
        return True
    if destination.startswith("#"):
        return True
    if destination.startswith("//"):
        return True
    if URI_SCHEME_RE.match(destination):
        return True
    return False


def resolve_candidate_path(file_path: Path, destination: str) -> Path:
    destination = destination.strip()
    if destination.startswith("<") and destination.endswith(">"):
        destination = destination[1:-1].strip()
    destination = destination.split("#", 1)[0].split("?", 1)[0].strip()
    destination = unquote(destination)
    destination = destination.replace("\\(", "(").replace("\\)", ")").replace("\\ ", " ")
    if destination.startswith("/"):
        return ROOT_DIR / destination.lstrip("/")
    return file_path.parent / destination


def check_file(file_path: Path) -> list[str]:
    text = file_path.read_text(encoding="utf-8", errors="replace")
    links, definitions = extract_links(text)
    failures: list[str] = []
    relative_file = file_path.relative_to(ROOT_DIR).as_posix()

    for link_type, raw_target in links:
        if link_type == "reference":
            key = normalize_reference_label(raw_target)
            target = definitions.get(key)
            if target is None:
                failures.append(f"{relative_file}: unresolved reference [{raw_target}]")
                continue
        else:
            target = raw_target

        target = target.strip()
        if should_skip_destination(target):
            continue

        candidate = resolve_candidate_path(file_path, target)
        if not candidate.exists():
            failures.append(f"{relative_file}: {target}")

    return failures


def main() -> int:
    markdown_files = sorted(ROOT_DIR.rglob("*.md"))
    broken_links: list[str] = []

    for file_path in markdown_files:
        broken_links.extend(check_file(file_path))

    if broken_links:
        print("Broken markdown links found:")
        for failure in broken_links:
            print(f" - {failure}")
        return 1

    print("No broken markdown links found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
