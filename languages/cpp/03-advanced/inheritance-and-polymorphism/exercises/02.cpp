#include <iostream>
#include <memory>
#include <vector>

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
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::unique_ptr<Shape>(new Rectangle(2.0, 5.0)));
    shapes.push_back(std::unique_ptr<Shape>(new Circle(1.5)));

    double totalArea = 0.0;
    for (const auto& shape : shapes) {
        totalArea += shape->area();
    }

    std::cout << "Total area: " << totalArea << '\n';
    return 0;
}
