// Module focus: Treating different concrete types through one common interface.
// Why it matters: practicing inheritance and polymorphism patterns makes exercises and checkpoints
// easier to reason about.

#include <iostream>
#include <memory>
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

// Walk through one fixed scenario so inheritance and polymorphism behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key inheritance and polymorphism path.
    vector<unique_ptr<Shape>> shapes;
    shapes.push_back(unique_ptr<Shape>(new Rectangle(3.0, 4.0)));
    shapes.push_back(unique_ptr<Shape>(new Circle(2.0)));

    for (const auto& shape : shapes) {
        // Report values so learners can verify the inheritance and polymorphism outcome.
        cout << "Area: " << shape->area() << '\n';
    }

    return 0;
}
