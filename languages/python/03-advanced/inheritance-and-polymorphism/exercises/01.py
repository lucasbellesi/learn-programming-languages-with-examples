from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self._base = base
        self._height = height

    def area(self) -> float:
        return 0.5 * self._base * self._height


parts = input("Enter base and height: ").strip().split()
if len(parts) != 2:
    print("Invalid input.")
else:
    try:
        base_value = float(parts[0])
        height_value = float(parts[1])
    except ValueError:
        print("Invalid input.")
    else:
        triangle = Triangle(base_value, height_value)
        print(f"Triangle area: {triangle.area()}")
