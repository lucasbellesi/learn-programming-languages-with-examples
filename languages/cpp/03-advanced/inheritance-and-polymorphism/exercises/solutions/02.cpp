#include <iostream>
#include <memory>
#include <string>
#include <vector>
using namespace std;

class Shape {
  public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
};

class Rectangle : public Shape {
  public:
    Rectangle(double widthValue, double heightValue) : width(widthValue), height(heightValue) {}

    double area() const override { return width * height; }

  private:
    double width;
    double height;
};

class Circle : public Shape {
  public:
    explicit Circle(double radiusValue) : radius(radiusValue) {}

    double area() const override { return 3.14159265358979323846 * radius * radius; }

  private:
    double radius;
};

int main() {
    int count = 0;
    if (!(cin >> count) || count < 0) {
        cout << "Expected a non-negative shape count.\n";
        return 0;
    }

    vector<unique_ptr<Shape>> shapes;
    for (int index = 0; index < count; ++index) {
        string kind;
        cin >> kind;
        if (kind == "rectangle") {
            double width = 0.0;
            double height = 0.0;
            if (!(cin >> width >> height)) {
                cout << "Invalid rectangle.\n";
                return 0;
            }
            shapes.push_back(unique_ptr<Shape>(new Rectangle(width, height)));
        } else if (kind == "circle") {
            double radius = 0.0;
            if (!(cin >> radius)) {
                cout << "Invalid circle.\n";
                return 0;
            }
            shapes.push_back(unique_ptr<Shape>(new Circle(radius)));
        } else {
            cout << "Unknown shape type.\n";
            return 0;
        }
    }

    double totalArea = 0.0;
    for (const auto& shape : shapes) {
        totalArea += shape->area();
    }

    cout << "Total area: " << totalArea << '\n';
    return 0;
}
