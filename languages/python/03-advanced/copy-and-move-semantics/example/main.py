# Example purpose: show the module flow with clear, beginner-friendly steps.


class Buffer:
    def __init__(self, size: int) -> None:
        safe_size = max(0, size)
        self._values = [0] * safe_size
        print(f"Constructed (size={len(self._values)})")

    @classmethod
    def _from_values(cls, values: list[int]) -> "Buffer":
        obj = cls(0)
        obj._values = values
        print(f"Transferred (size={len(values)})")
        return obj

    def clone(self) -> "Buffer":
        # Intent: deep copy isolates future changes between instances.
        cloned = Buffer(0)
        cloned._values = self._values.copy()
        print("Cloned")
        return cloned

    def transfer(self) -> "Buffer":
        # Intent: transfer operation hands over current data and resets source.
        moved_values = self._values
        self._values = []
        return Buffer._from_values(moved_values)

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
