# This helper example focuses on isolating one polymorphic dispatch path so the common interface
# stays clear.

# This extra example extends inheritance-and-polymorphism with a polymorphic menu.

# Keep this helper separate so the main example can focus on the larger idea without extra noise.
class Shape:
    def area(self):
        raise NotImplementedError

    def name(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415926535 * self.radius * self.radius

    def name(self):
        return "Circle"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def name(self):
        return "Rectangle"


shapes = []

while True:
    print("\nMenu")
    print("1) Add circle")
    print("2) Add rectangle")
    print("3) List areas")
    print("4) Exit")

    option = input("Choose: ").strip()

    if option == "1":
        raw_radius = input("Radius: ").strip()
        try:
            radius = float(raw_radius)
        except ValueError:
            print("Radius must be positive.")
            continue

        if radius > 0.0:
            shapes.append(Circle(radius))
        else:
            print("Radius must be positive.")
    elif option == "2":
        raw_width = input("Width: ").strip()
        raw_height = input("Height: ").strip()
        try:
            width = float(raw_width)
            height = float(raw_height)
        except ValueError:
            print("Width and height must be positive.")
            continue

        if width > 0.0 and height > 0.0:
            shapes.append(Rectangle(width, height))
        else:
            print("Width and height must be positive.")
    elif option == "3":
        if not shapes:
            print("No shapes added yet.")
            continue

        total_area = 0.0
        for shape in shapes:
            shape_area = shape.area()
            total_area += shape_area
            print(f"- {shape.name()} area: {shape_area}")
        print(f"Total area: {total_area}")
    elif option == "4":
        print("Goodbye.")
        break
    else:
        print("Invalid option.")
