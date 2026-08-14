from __future__ import annotations

import time


def measure(action) -> float:
    start = time.perf_counter()
    action()
    return time.perf_counter() - start


def fill_without_presize(count: int) -> list[int]:
    values: list[int] = []
    for index in range(count):
        values.append(index)
    return values


def fill_with_presize(count: int) -> list[int]:
    values = [0] * count
    for index in range(count):
        values[index] = index
    return values


def main() -> None:
    try:
        count = int(input("Element count: "))
    except ValueError:
        print("Invalid element count.")
        return

    if count < 0:
        print("Element count cannot be negative.")
        return

    no_presize = measure(lambda: fill_without_presize(count))
    with_presize = measure(lambda: fill_with_presize(count))
    print(f"Without pre-size: {no_presize:.6f}s")
    print(f"With pre-size: {with_presize:.6f}s")


if __name__ == "__main__":
    main()
