# Example purpose: compare a couple of small optimization choices with simple timings.

from __future__ import annotations

import time


def measure(action) -> float:
    start = time.perf_counter()
    action()
    return time.perf_counter() - start


def build_with_concatenation(line_count: int) -> str:
    text = ""
    for index in range(line_count):
        text += f"row-{index};"
    return text


def build_with_join(line_count: int) -> str:
    parts = [f"row-{index};" for index in range(line_count)]
    return "".join(parts)


def fill_without_presize(item_count: int) -> list[int]:
    values: list[int] = []
    for index in range(item_count):
        values.append(index)
    return values


def fill_with_presize(item_count: int) -> list[int]:
    values = [0] * item_count
    for index in range(item_count):
        values[index] = index
    return values


def main() -> None:
    # Program flow: measure two paired implementations on the same workload size.
    line_count = 4_000
    concat_duration = measure(lambda: build_with_concatenation(line_count))
    join_duration = measure(lambda: build_with_join(line_count))

    print(f"String concatenation: {concat_duration:.6f}s")
    print(f"str.join: {join_duration:.6f}s")

    item_count = 200_000
    no_presize = measure(lambda: fill_without_presize(item_count))
    with_presize = measure(lambda: fill_with_presize(item_count))

    # Intent: final output keeps the comparison direct and easy to verify.
    print(f"List fill without pre-size: {no_presize:.6f}s")
    print(f"List fill with pre-size: {with_presize:.6f}s")


if __name__ == "__main__":
    main()
