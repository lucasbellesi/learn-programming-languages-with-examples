# This example shows writing generic code that stays useful across multiple data types.
# In Python, the example favors direct readable steps while keeping validation visible.

from typing import Generic, TypeVar

# Build the sample state first, then let the later output confirm the behavior step by step.
T = TypeVar("T")


# Define the reusable pieces first so the main flow can focus on one observable scenario.
def max_value(left: T, right: T) -> T:
    return left if left > right else right


class Pair(Generic[T]):
    def __init__(self, first: T, second: T) -> None:
        self._first = first
        self._second = second

    def print(self) -> None:
        print(f"({self._first}, {self._second})")


# Run one deterministic scenario so the console output makes writing generic code that stays useful
# across multiple data types easy to verify.
def main() -> None:
    print(f"max_value(4, 7) = {max_value(4, 7)}")
    print(f"max_value(2.5, 1.2) = {max_value(2.5, 1.2)}")

    pair = Pair[str]("left", "right")
    pair.print()


if __name__ == "__main__":
    main()
