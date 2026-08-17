# Module focus: How copying, sharing, or transferring state changes later behavior.
# Why it matters: the example makes it possible to predict aliasing and independence after
# copying or sharing values before the learner tackles the exercises.

# Separate helpers keep the main path focused on how to predict aliasing and independence after
# copying or sharing values.
class Buffer:
    def __init__(self, size: int) -> None:
        # These values exercise the normal path before the exercises vary the documented
        # boundaries.
        safe_size = max(0, size)
        self._values = [0] * safe_size
        # The printed result shows whether the program can choose an idiomatic ownership-transfer
        # strategy for the language.
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


# Fixed inputs make the consequence of assuming `=` duplicates list contents visible and
# repeatable.
def main() -> None:
    first = Buffer(3)
    second = first.clone()
    third = second.transfer()

    print(f"first size: {first.size}")
    print(f"second size (after transfer): {second.size}")
    print(f"third size: {third.size}")


if __name__ == "__main__":
    main()
