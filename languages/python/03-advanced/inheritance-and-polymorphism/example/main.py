# This example shows treating different concrete types through one common interface.
# In Python, the example favors direct readable steps while keeping validation visible.

from abc import ABC, abstractmethod
from math import pi


# Define the reusable pieces first so the main flow can focus on one observable scenario.
class Shape(ABC):
    # Build the sample state first, then let the later output confirm the behavior step by step.
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


# Run one deterministic scenario so the console output makes treating different concrete types
# through one common interface easy to verify.
def main() -> None:
    shapes: list[Shape] = [Rectangle(3.0, 4.0), Circle(2.0)]

    for shape in shapes:
        print(f"{shape.name} area: {shape.area():.2f}")


if __name__ == "__main__":
    main()
