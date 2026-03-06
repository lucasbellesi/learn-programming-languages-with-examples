#include <iostream>
using namespace std;


void printRangeSum(int from, int to) {
    int sum = 0;
    for (int value = from; value <= to; ++value) {
        sum += value;
    }
    cout << "Sum from " << from << " to " << to << " = " << sum << '\n';
}

int main() {
    int value = 10;
    cout << "Outer value: " << value << '\n';

    {
        int value = 20;
        cout << "Inner shadowed value: " << value << '\n';
    }

    cout << "Outer value again: " << value << '\n';

    printRangeSum(1, 5);
    return 0;
}
