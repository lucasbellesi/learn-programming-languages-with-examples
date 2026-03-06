#include <iostream>

class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
};

class Triangle : public Shape {
public:
    Triangle(double baseValue, double heightValue) : base(baseValue), height(heightValue) {}

    double area() const override {
        return 0.5 * base * height;
    }

private:
    double base;
    double height;
};

int main() {
    double base = 0.0;
    double height = 0.0;
    std::cout << "Enter base and height: ";
    std::cin >> base >> height;

    Triangle triangle(base, height);
    std::cout << "Triangle area: " << triangle.area() << '\n';
    return 0;
}
