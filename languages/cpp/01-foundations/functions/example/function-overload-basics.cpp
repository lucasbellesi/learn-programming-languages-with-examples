#include <iostream>
#include <string>

using namespace std;

void printValue(int value) {
    cout << "Integer value: " << value << '\n';
}

void printValue(double value) {
    cout << "Double value: " << value << '\n';
}

void printValue(const string& value) {
    cout << "String value: " << value << '\n';
}

int main() {
    printValue(42);
    printValue(3.14159);
    printValue("Hello from function overloads");

    return 0;
}
