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
    vector<unique_ptr<Shape>> shapes;
    shapes.push_back(unique_ptr<Shape>(new Rectangle(3.0, 4.0)));
    shapes.push_back(unique_ptr<Shape>(new Circle(2.0)));

    for (const auto& shape : shapes) {
        cout << "Area: " << shape->area() << '\n';
    }

    return 0;
}
