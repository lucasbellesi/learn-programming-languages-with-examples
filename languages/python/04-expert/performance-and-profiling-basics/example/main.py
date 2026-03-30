# Example purpose: compare a couple of small optimization choices with simple timings.

from __future__ import annotations

import time


retained_object: object | None = None


def measure_average(action, repetitions: int) -> float:
    action()

    total = 0.0
    for _ in range(repetitions):
        start = time.perf_counter()
        action()
        total += time.perf_counter() - start
    return total / repetitions


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
    repetitions = 12

    def remember(value: object) -> None:
        global retained_object
        retained_object = value

    concat_duration = measure_average(
        lambda: remember(build_with_concatenation(line_count)),
        repetitions,
    )
    join_duration = measure_average(
        lambda: remember(build_with_join(line_count)),
        repetitions,
    )

    print(f"Average string concatenation ({repetitions} runs): {concat_duration:.6f}s")
    print(f"Average str.join ({repetitions} runs): {join_duration:.6f}s")

    item_count = 200_000
    no_presize = measure_average(
        lambda: remember(fill_without_presize(item_count)),
        repetitions,
    )
    with_presize = measure_average(
        lambda: remember(fill_with_presize(item_count)),
        repetitions,
    )

    # Intent: final output keeps the comparison direct and easy to verify.
    print(f"Average list fill without pre-size ({repetitions} runs): {no_presize:.6f}s")
    print(f"Average list fill with pre-size ({repetitions} runs): {with_presize:.6f}s")


if __name__ == "__main__":
    main()
