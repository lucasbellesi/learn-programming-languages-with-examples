#include <iostream>
using namespace std;


struct Rectangle {
    double width;
    double height;

    double area() const {
        return width * height;
    }

    double perimeter() const {
        return 2.0 * (width + height);
    }
};

int main() {
    Rectangle rectangle{0.0, 0.0};

    cout << "Enter width and height: ";
    cin >> rectangle.width >> rectangle.height;

    if (rectangle.width <= 0.0 || rectangle.height <= 0.0) {
        cout << "Width and height must be positive.\n";
        return 0;
    }

    cout << "Area: " << rectangle.area() << '\n';
    cout << "Perimeter: " << rectangle.perimeter() << '\n';
    return 0;
}
