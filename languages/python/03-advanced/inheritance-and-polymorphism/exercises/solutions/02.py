from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self._radius = radius

    def area(self) -> float:
        return pi * self._radius * self._radius


shapes: list[Shape] = [Rectangle(2.0, 5.0), Circle(1.5)]

total_area = 0.0
for shape in shapes:
    total_area += shape.area()

print(f"Total area: {total_area}")
