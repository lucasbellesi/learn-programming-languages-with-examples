// This example demonstrates inheritance and polymorphism concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

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

    double area() const override {
        return width * height;
    }

private:
    double width;
    double height;
};

class Circle : public Shape {
public:
    explicit Circle(double radiusValue) : radius(radiusValue) {}

    double area() const override {
        return 3.14159265358979323846 * radius * radius;
    }

private:
    double radius;
};

int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    vector<unique_ptr<Shape>> shapes;
    shapes.push_back(unique_ptr<Shape>(new Rectangle(3.0, 4.0)));
    shapes.push_back(unique_ptr<Shape>(new Circle(2.0)));

    // Intent: iterate through data in a clear and deterministic order.
    for (const auto& shape : shapes) {
        // Intent: print intermediate or final output for quick behavior verification.
        cout << "Area: " << shape->area() << '\n';
    }

    return 0;
}
