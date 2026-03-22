# Example purpose: show the module flow with clear, beginner-friendly steps.

from typing import Generic, TypeVar

T = TypeVar("T")


def max_value(left: T, right: T) -> T:
    return left if left > right else right


class Pair(Generic[T]):
    def __init__(self, first: T, second: T) -> None:
        self._first = first
        self._second = second

    def print(self) -> None:
        # Intent: print final state from a generic container in one predictable format.
        print(f"({self._first}, {self._second})")


def main() -> None:
    # Program flow: call one generic helper, then inspect one generic class instance.
    print(f"max_value(4, 7) = {max_value(4, 7)}")
    print(f"max_value(2.5, 1.2) = {max_value(2.5, 1.2)}")

    pair = Pair[str]("left", "right")
    pair.print()


if __name__ == "__main__":
    main()
