# Example purpose: show the module flow with clear, beginner-friendly steps.

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
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


def main() -> None:
    # Program flow: create mixed shapes and evaluate them through one base contract.
    shapes: list[Shape] = [Rectangle(3.0, 4.0), Circle(2.0)]

    # Intent: polymorphic iteration keeps logic independent from concrete classes.
    for shape in shapes:
        print(f"{shape.name} area: {shape.area():.2f}")


if __name__ == "__main__":
    main()
