// This example shows treating different concrete types through one common interface.
// In C++, the example keeps value flow, references, and explicit control visible.

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

// Run one deterministic scenario so the console output makes treating different concrete types
// through one common interface easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    vector<unique_ptr<Shape>> shapes;
    shapes.push_back(unique_ptr<Shape>(new Rectangle(3.0, 4.0)));
    shapes.push_back(unique_ptr<Shape>(new Circle(2.0)));

    for (const auto& shape : shapes) {
        // Print the observed state here so learners can connect the code path to a concrete result.
        cout << "Area: " << shape->area() << '\n';
    }

    return 0;
}
