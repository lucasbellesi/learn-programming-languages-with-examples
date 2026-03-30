from __future__ import annotations

import time


def measure(action) -> float:
    start = time.perf_counter()
    action()
    return time.perf_counter() - start


def build_with_concatenation(line_count: int) -> str:
    text = ""
    for index in range(line_count):
        text += f"item-{index};"
    return text


def build_with_join(line_count: int) -> str:
    return "".join(f"item-{index};" for index in range(line_count))


def main() -> None:
    try:
        line_count = int(input("Line count: "))
    except ValueError:
        print("Invalid line count.")
        return

    if line_count < 0:
        print("Line count cannot be negative.")
        return

    concat_duration = measure(lambda: build_with_concatenation(line_count))
    join_duration = measure(lambda: build_with_join(line_count))
    print(f"Concatenation: {concat_duration:.6f}s")
    print(f"Join: {join_duration:.6f}s")


if __name__ == "__main__":
    main()
