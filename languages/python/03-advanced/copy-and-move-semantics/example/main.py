# Example purpose: show the module flow with clear, beginner-friendly steps.


class Buffer:
    def __init__(self, size: int) -> None:
        safe_size = max(0, size)
        self._values = [0] * safe_size
        print(f"Constructed (size={len(self._values)})")

    def clone(self) -> "Buffer":
        # Intent: deep copy isolates future changes between instances.
        cloned = Buffer.__new__(Buffer)
        cloned._values = self._values.copy()
        print("Cloned")
        return cloned

    def transfer(self) -> "Buffer":
        # Intent: transfer operation hands over current data and resets source.
        moved_values = self._values
        self._values = []
        transferred = Buffer.__new__(Buffer)
        transferred._values = moved_values
        print(f"Transferred (size={len(moved_values)})")
        return transferred

    @property
    def size(self) -> int:
        return len(self._values)


def main() -> None:
    # Program flow: create, clone, transfer, then inspect resulting states.
    first = Buffer(3)
    second = first.clone()
    third = second.transfer()

    print(f"first size: {first.size}")
    print(f"second size (after transfer): {second.size}")
    print(f"third size: {third.size}")


if __name__ == "__main__":
    main()
