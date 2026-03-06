#include <iostream>
using namespace std;


int maxOfThree(int a, int b, int c) {
    int currentMax = a;
    if (b > currentMax) {
        currentMax = b;
    }
    if (c > currentMax) {
        currentMax = c;
    }
    return currentMax;
}

int main() {
    int x = 0;
    int y = 0;
    int z = 0;

    cout << "Enter three integers: ";
    cin >> x >> y >> z;

    cout << "Maximum: " << maxOfThree(x, y, z) << '\n';
    return 0;
}
