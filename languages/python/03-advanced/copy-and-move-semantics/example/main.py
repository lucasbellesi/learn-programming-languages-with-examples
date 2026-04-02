# Module focus: How copying, sharing, or transferring state changes later behavior.
# Why it matters: practicing copy and move semantics patterns makes exercises and checkpoints easier
# to reason about.

# Helper setup for copy and move semantics; this keeps the walkthrough readable.
class Buffer:
    def __init__(self, size: int) -> None:
        # Prepare sample inputs that exercise the key copy and move semantics path.
        safe_size = max(0, size)
        self._values = [0] * safe_size
        # Report output values so learners can verify the copy and move semantics outcome.
        print(f"Constructed (size={len(self._values)})")

    def clone(self) -> "Buffer":
        cloned = Buffer.__new__(Buffer)
        cloned._values = self._values.copy()
        print("Cloned")
        return cloned

    def transfer(self) -> "Buffer":
        moved_values = self._values
        self._values = []
        transferred = Buffer.__new__(Buffer)
        transferred._values = moved_values
        print(f"Transferred (size={len(moved_values)})")
        return transferred

    @property
    def size(self) -> int:
        return len(self._values)


# Walk through one fixed scenario so copy and move semantics behavior stays repeatable.
def main() -> None:
    first = Buffer(3)
    second = first.clone()
    third = second.transfer()

    print(f"first size: {first.size}")
    print(f"second size (after transfer): {second.size}")
    print(f"third size: {third.size}")


if __name__ == "__main__":
    main()
