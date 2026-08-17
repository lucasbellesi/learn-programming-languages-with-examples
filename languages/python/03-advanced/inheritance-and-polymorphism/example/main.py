# Module focus: Treating different concrete types through one common interface.
# Why it matters: the example makes it possible to program against a shared behavioral
# abstraction before the learner tackles the exercises.

from abc import ABC, abstractmethod
from math import pi


# Separate helpers keep the main path focused on how to program against a shared behavioral
# abstraction.
class Shape(ABC):
    # These values exercise the normal path before the exercises vary the documented boundaries.
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


# Fixed inputs make the consequence of forgetting to implement required abstract methods visible
# and repeatable.
def main() -> None:
    shapes: list[Shape] = [Rectangle(3.0, 4.0), Circle(2.0)]

    for shape in shapes:
        # The printed result shows whether the program can use dynamic dispatch without unsafe
        # type assumptions.
        print(f"{shape.name} area: {shape.area():.2f}")


if __name__ == "__main__":
    main()
