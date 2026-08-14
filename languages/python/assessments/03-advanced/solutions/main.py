from __future__ import annotations

import math
from typing import TypeVar


class Shape:
    def area(self) -> float:
        raise NotImplementedError

    def name(self) -> str:
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self._radius = radius

    def area(self) -> float:
        return math.pi * self._radius * self._radius

    def name(self) -> str:
        return "Circle"


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

    def name(self) -> str:
        return "Rectangle"


T = TypeVar("T")


def print_list(values: list[T], label: str) -> None:
    rendered = ", ".join(str(value) for value in values)
    print(f"{label}: [{rendered}]")


def main() -> None:
    shapes: list[Shape] = [
        Circle(2.0),
        Rectangle(3.0, 4.0),
        Circle(1.5),
    ]

    areas: list[float] = []

    print("Shape areas:")
    for shape in shapes:
        value = shape.area()
        areas.append(value)
        print(f"- {shape.name()}: {value}")

    total_area = sum(areas)
    min_area = min(areas)
    max_area = max(areas)

    print(f"Total area: {total_area}")
    print(f"Minimum area: {min_area}")
    print(f"Maximum area: {max_area}")

    print_list([1, 2, 3, 4], "Sample counts")
    print_list(areas, "Computed areas")


if __name__ == "__main__":
    main()
