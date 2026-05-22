# Module focus: Measuring hot paths before changing code for speed.
# Why it matters: practicing performance and profiling basics patterns makes exercises and
# checkpoints easier to reason about.

from __future__ import annotations

import time

# Prepare sample inputs that exercise the key performance and profiling basics path.
retained_object: object | None = None


# Helper setup for performance and profiling basics; this keeps the walkthrough readable.
def measure_average(action, repetitions: int) -> float:
    # Warm up once so setup effects are less likely to dominate the repeated samples.
    action()

    total = 0.0
    for _ in range(repetitions):
        start = time.perf_counter()
        action()
        total += time.perf_counter() - start
    return total / repetitions


def build_with_concatenation(line_count: int) -> str:
    # Repeated concatenation creates new strings as the result grows.
    text = ""
    for index in range(line_count):
        text += f"row-{index};"
    return text


def build_with_join(line_count: int) -> str:
    # Building parts first lets join allocate the final string once.
    parts = [f"row-{index};" for index in range(line_count)]
    return "".join(parts)


def fill_without_presize(item_count: int) -> list[int]:
    values: list[int] = []
    for index in range(item_count):
        values.append(index)
    return values


def fill_with_presize(item_count: int) -> list[int]:
    # Pre-sizing makes the target length explicit before assignments begin.
    values = [0] * item_count
    for index in range(item_count):
        values[index] = index
    return values


# Walk through one fixed scenario so performance and profiling basics behavior stays repeatable.
def main() -> None:
    line_count = 4_000
    repetitions = 12

    def remember(value: object) -> None:
        # Keep results alive so the benchmark still performs real work.
        global retained_object
        retained_object = value

    # Measure two implementations of the same string-building task.
    concat_duration = measure_average(
        lambda: remember(build_with_concatenation(line_count)),
        repetitions,
    )
    join_duration = measure_average(
        lambda: remember(build_with_join(line_count)),
        repetitions,
    )

    # Report output values so learners can verify the performance and profiling basics outcome.
    print(f"Average string concatenation ({repetitions} runs): {concat_duration:.6f}s")
    print(f"Average str.join ({repetitions} runs): {join_duration:.6f}s")

    item_count = 200_000
    # Repeat the same measurement shape for list growth strategies.
    no_presize = measure_average(
        lambda: remember(fill_without_presize(item_count)),
        repetitions,
    )
    with_presize = measure_average(
        lambda: remember(fill_with_presize(item_count)),
        repetitions,
    )

    print(f"Average list fill without pre-size ({repetitions} runs): {no_presize:.6f}s")
    print(f"Average list fill with pre-size ({repetitions} runs): {with_presize:.6f}s")


if __name__ == "__main__":
    main()
