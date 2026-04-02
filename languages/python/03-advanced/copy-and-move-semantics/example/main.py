# This example shows how copying, sharing, or transferring state changes later behavior.
# In Python, the example favors direct readable steps while keeping validation visible.

# Define the reusable pieces first so the main flow can focus on one observable scenario.
class Buffer:
    def __init__(self, size: int) -> None:
        # Build the sample state first, then let the later output confirm the behavior step by step.
        safe_size = max(0, size)
        self._values = [0] * safe_size
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


# Run one deterministic scenario so the console output makes how copying, sharing, or transferring
# state changes later behavior easy to verify.
def main() -> None:
    first = Buffer(3)
    second = first.clone()
    third = second.transfer()

    print(f"first size: {first.size}")
    print(f"second size (after transfer): {second.size}")
    print(f"third size: {third.size}")


if __name__ == "__main__":
    main()
