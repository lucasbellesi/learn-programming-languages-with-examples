// This helper example focuses on isolating one polymorphic dispatch path so the common interface
// stays clear.

#include <iostream>
#include <memory>
#include <vector>

using namespace std;

class Shape {
  public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
    virtual const char* name() const = 0;
};

class Circle : public Shape {
  public:
    explicit Circle(double radiusValue) : radius(radiusValue) {}

    double area() const override { return 3.1415926535 * radius * radius; }

    const char* name() const override { return "Circle"; }

  private:
    double radius;
};

class Rectangle : public Shape {
  public:
    Rectangle(double widthValue, double heightValue) : width(widthValue), height(heightValue) {}

    double area() const override { return width * height; }

    const char* name() const override { return "Rectangle"; }

  private:
    double width;
    double height;
};

int main() {
    vector<unique_ptr<Shape>> shapes;

    while (true) {
        int option = 0;
        cout << "\nMenu\n";
        cout << "1) Add circle\n";
        cout << "2) Add rectangle\n";
        cout << "3) List areas\n";
        cout << "4) Exit\n";
        cout << "Choose: ";
        cin >> option;

        if (option == 1) {
            double radius = 0.0;
            cout << "Radius: ";
            cin >> radius;
            if (radius > 0.0) {
                shapes.push_back(make_unique<Circle>(radius));
            } else {
                cout << "Radius must be positive.\n";
            }
        } else if (option == 2) {
            double width = 0.0;
            double height = 0.0;
            cout << "Width: ";
            cin >> width;
            cout << "Height: ";
            cin >> height;
            if (width > 0.0 && height > 0.0) {
                shapes.push_back(make_unique<Rectangle>(width, height));
            } else {
                cout << "Width and height must be positive.\n";
            }
        } else if (option == 3) {
            if (shapes.empty()) {
                cout << "No shapes added yet.\n";
                continue;
            }

            double totalArea = 0.0;
            for (const unique_ptr<Shape>& shape : shapes) {
                const double shapeArea = shape->area();
                totalArea += shapeArea;
                cout << "- " << shape->name() << " area: " << shapeArea << '\n';
            }
            cout << "Total area: " << totalArea << '\n';
        } else if (option == 4) {
            cout << "Goodbye.\n";
            break;
        } else {
            cout << "Invalid option.\n";
        }
    }

    return 0;
}
