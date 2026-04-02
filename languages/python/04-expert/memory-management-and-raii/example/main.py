# This example shows tying resource cleanup to object lifetime so cleanup stays predictable.
# In Python, the example favors direct readable steps while keeping validation visible.

from __future__ import annotations


# Define the reusable pieces first so the main flow can focus on one observable scenario.
class BufferLease:
    # Build the sample state first, then let the later output confirm the behavior step by step.
    active_leases = 0

    def __init__(self, name: str, size: int) -> None:
        self._name = name
        self._values = [0] * size
        self._closed = False

    def __enter__(self) -> "BufferLease":
        BufferLease.active_leases += 1
        print(f"[acquire] {self._name} size={len(self._values)} active={BufferLease.active_leases}")
        return self

    def __exit__(self, exc_type, exc, exc_tb) -> None:
        self.close()

    def fill_sequence(self, start: int, step: int) -> None:
        self._ensure_open()
        for index in range(len(self._values)):
            self._values[index] = start + (index * step)

    def total(self) -> int:
        self._ensure_open()
        return sum(self._values)

    def describe(self) -> str:
        self._ensure_open()
        return " ".join(str(value) for value in self._values)

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self._values.clear()
        BufferLease.active_leases -= 1
        print(f"[close] {self._name} active={BufferLease.active_leases}")

    def _ensure_open(self) -> None:
        if self._closed:
            raise RuntimeError("buffer already closed")


# Run one deterministic scenario so the console output makes tying resource cleanup to object
# lifetime so cleanup stays predictable easy to verify.
def main() -> None:
    print(f"Active before scope: {BufferLease.active_leases}")

    with BufferLease("scores", 5) as scores:
        scores.fill_sequence(10, 5)
        print(f"Scores: {scores.describe()}")
        print(f"Sum: {scores.total()}")

        with BufferLease("scratch", 3) as scratch:
            scratch.fill_sequence(1, 1)
            print(f"Scratch: {scratch.describe()}")
            print(f"Active inside scope: {BufferLease.active_leases}")

    print(f"Active after scope: {BufferLease.active_leases}")


if __name__ == "__main__":
    main()
