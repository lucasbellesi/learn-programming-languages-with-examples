# Module focus: Writing generic code that stays useful across multiple data types.
# Why it matters: the example makes it possible to express reusable type-safe behavior with
# language generics before the learner tackles the exercises.

from typing import Generic, TypeVar

# These values exercise the normal path before the exercises vary the documented boundaries.
T = TypeVar("T")


# Separate helpers keep the main path focused on how to express reusable type-safe behavior with
# language generics.
def max_value(left: T, right: T) -> T:
    return left if left > right else right


class Pair(Generic[T]):
    def __init__(self, first: T, second: T) -> None:
        self._first = first
        self._second = second

    def print(self) -> None:
        # The printed result shows whether the program can apply constraints when an operation
        # requires specific capabilities.
        print(f"({self._first}, {self._second})")


# Fixed inputs make the consequence of assuming type hints enforce runtime behavior by themselves
# visible and repeatable.
def main() -> None:
    print(f"max_value(4, 7) = {max_value(4, 7)}")
    print(f"max_value(2.5, 1.2) = {max_value(2.5, 1.2)}")

    pair = Pair[str]("left", "right")
    pair.print()


if __name__ == "__main__":
    main()
