from __future__ import annotations

import time


class Step:
    def __init__(self, name: str) -> None:
        self._name = name
        self._processed_count = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def processed_count(self) -> int:
        return self._processed_count

    def run(self) -> None:
        self._processed_count += 1


def main() -> None:
    job_count = 3
    steps = [Step("load"), Step("transform")]

    start = time.perf_counter()

    for _ in range(job_count):
        for step in steps:
            step.run()

    elapsed_microseconds = int((time.perf_counter() - start) * 1_000_000)

    print(f"Running {job_count} jobs through {len(steps)} steps...")
    for step in steps:
        print(f"Step {step.name} processed {step.processed_count} jobs")
    print(f"Elapsed (microseconds): {elapsed_microseconds}")


if __name__ == "__main__":
    main()
