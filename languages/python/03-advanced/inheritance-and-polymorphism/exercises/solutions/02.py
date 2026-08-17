from abc import ABC, abstractmethod
from math import pi
import sys


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


tokens = sys.stdin.read().split()
try:
    count = int(tokens[0])
except (IndexError, ValueError):
    print("Expected a non-negative shape count.")
    raise SystemExit(0)

if count < 0:
    print("Expected a non-negative shape count.")
    raise SystemExit(0)

shapes: list[Shape] = []
cursor = 1
for _ in range(count):
    try:
        kind = tokens[cursor]
        cursor += 1
        if kind == "rectangle":
            width = float(tokens[cursor])
            height = float(tokens[cursor + 1])
            cursor += 2
            shapes.append(Rectangle(width, height))
        elif kind == "circle":
            radius = float(tokens[cursor])
            cursor += 1
            shapes.append(Circle(radius))
        else:
            print("Unknown shape type.")
            raise SystemExit(0)
    except (IndexError, ValueError):
        print("Invalid shape data.")
        raise SystemExit(0)

total_area = 0.0
for shape in shapes:
    total_area += shape.area()

print(f"Total area: {total_area}")
