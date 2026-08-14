class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2.0 * (self.width + self.height)


raw = input("Enter width and height: ").strip().split()
if len(raw) != 2:
    print("Invalid input. Enter exactly two numbers.")
else:
    try:
        width = float(raw[0])
        height = float(raw[1])
    except ValueError:
        print("Invalid input. Enter exactly two numbers.")
    else:
        if width <= 0 or height <= 0:
            print("Width and height must be positive.")
        else:
            rectangle = Rectangle(width, height)
            print(f"Area: {rectangle.area()}")
            print(f"Perimeter: {rectangle.perimeter()}")
