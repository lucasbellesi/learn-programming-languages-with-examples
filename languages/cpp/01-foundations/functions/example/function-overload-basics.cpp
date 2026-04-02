// This helper example focuses on showing one focused overload or helper so the main example stays
// easy to scan.

#include <iostream>
#include <string>

using namespace std;

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
void printValue(int value) { cout << "Integer value: " << value << '\n'; }

void printValue(double value) { cout << "Double value: " << value << '\n'; }

void printValue(const string& value) { cout << "String value: " << value << '\n'; }

int main() {
    printValue(42);
    printValue(3.14159);
    printValue("Hello from function overloads");

    return 0;
}
