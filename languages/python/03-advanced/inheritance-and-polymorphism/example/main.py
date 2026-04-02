# Module focus: Treating different concrete types through one common interface.
# Why it matters: practicing inheritance and polymorphism patterns makes exercises and checkpoints
# easier to reason about.

from abc import ABC, abstractmethod
from math import pi


# Helper setup for inheritance and polymorphism; this keeps the walkthrough readable.
class Shape(ABC):
    # Prepare sample inputs that exercise the key inheritance and polymorphism path.
    @abstractmethod
    def area(self) -> float:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

    @property
    def name(self) -> str:
        return "Rectangle"


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self._radius = radius

    def area(self) -> float:
        return pi * self._radius * self._radius

    @property
    def name(self) -> str:
        return "Circle"


# Walk through one fixed scenario so inheritance and polymorphism behavior stays repeatable.
def main() -> None:
    shapes: list[Shape] = [Rectangle(3.0, 4.0), Circle(2.0)]

    for shape in shapes:
        # Report output values so learners can verify the inheritance and polymorphism outcome.
        print(f"{shape.name} area: {shape.area():.2f}")


if __name__ == "__main__":
    main()
