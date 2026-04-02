# Module focus: Writing generic code that stays useful across multiple data types.
# Why it matters: practicing templates basics patterns makes exercises and checkpoints easier to
# reason about.

from typing import Generic, TypeVar

# Prepare sample inputs that exercise the key templates basics path.
T = TypeVar("T")


# Helper setup for templates basics; this keeps the walkthrough readable.
def max_value(left: T, right: T) -> T:
    return left if left > right else right


class Pair(Generic[T]):
    def __init__(self, first: T, second: T) -> None:
        self._first = first
        self._second = second

    def print(self) -> None:
        # Report output values so learners can verify the templates basics outcome.
        print(f"({self._first}, {self._second})")


# Walk through one fixed scenario so templates basics behavior stays repeatable.
def main() -> None:
    print(f"max_value(4, 7) = {max_value(4, 7)}")
    print(f"max_value(2.5, 1.2) = {max_value(2.5, 1.2)}")

    pair = Pair[str]("left", "right")
    pair.print()


if __name__ == "__main__":
    main()
