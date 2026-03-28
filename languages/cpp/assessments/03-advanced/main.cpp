#include <algorithm>
#include <numeric>
#include <cmath>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

using namespace std;

class Shape {
  public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
    virtual string name() const = 0;
};

class Circle : public Shape {
  public:
    explicit Circle(double radiusValue) : radius(radiusValue) {}

    double area() const override { return 3.141592653589793 * radius * radius; }

    string name() const override { return "Circle"; }

  private:
    double radius;
};

class Rectangle : public Shape {
  public:
    Rectangle(double widthValue, double heightValue) : width(widthValue), height(heightValue) {}

    double area() const override { return width * height; }

    string name() const override { return "Rectangle"; }

  private:
    double width;
    double height;
};

template <typename T> void printVector(const vector<T>& values, const string& label) {
    cout << label << ": [";
    for (size_t i = 0; i < values.size(); ++i) {
        cout << values[i];
        if (i + 1 < values.size()) {
            cout << ", ";
        }
    }
    cout << "]\n";
}

int main() {
    vector<unique_ptr<Shape>> shapes;
    shapes.push_back(make_unique<Circle>(2.0));
    shapes.push_back(make_unique<Rectangle>(3.0, 4.0));
    shapes.push_back(make_unique<Circle>(1.5));

    vector<double> areas;
    areas.reserve(shapes.size());

    cout << "Shape areas:\n";
    for (const unique_ptr<Shape>& shape : shapes) {
        const double value = shape->area();
        areas.push_back(value);
        cout << "- " << shape->name() << ": " << value << '\n';
    }

    const double totalArea = accumulate(areas.begin(), areas.end(), 0.0);
    const double minArea = *min_element(areas.begin(), areas.end());
    const double maxArea = *max_element(areas.begin(), areas.end());

    cout << "Total area: " << totalArea << '\n';
    cout << "Minimum area: " << minArea << '\n';
    cout << "Maximum area: " << maxArea << '\n';

    vector<int> sampleCounts = {1, 2, 3, 4};
    printVector(sampleCounts, "Sample counts");
    printVector(areas, "Computed areas");

    return 0;
}
