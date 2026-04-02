# Module focus: Tying resource cleanup to object lifetime so cleanup stays predictable.
# Why it matters: practicing memory management and raii patterns makes exercises and checkpoints
# easier to reason about.

from __future__ import annotations


# Helper setup for memory management and raii; this keeps the walkthrough readable.
class BufferLease:
    # Prepare sample inputs that exercise the key memory management and raii path.
    active_leases = 0

    def __init__(self, name: str, size: int) -> None:
        self._name = name
        self._values = [0] * size
        self._closed = False

    def __enter__(self) -> "BufferLease":
        BufferLease.active_leases += 1
        # Report output values so learners can verify the memory management and raii outcome.
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


# Walk through one fixed scenario so memory management and raii behavior stays repeatable.
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
