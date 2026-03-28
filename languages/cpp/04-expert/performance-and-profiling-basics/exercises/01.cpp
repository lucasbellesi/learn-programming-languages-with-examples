#include <chrono>
#include <iostream>
#include <vector>
using namespace std;

long long sumByValue(vector<int> values) {
    long long sum = 0;
    for (int value : values) {
        sum += value;
    }
    return sum;
}

long long sumByConstRef(const vector<int>& values) {
    long long sum = 0;
    for (int value : values) {
        sum += value;
    }
    return sum;
}

int main() {
    int n = 0;
    cout << "Vector size: ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive size.\n";
        return 0;
    }

    vector<int> values(static_cast<size_t>(n), 1);

    const auto startValue = chrono::high_resolution_clock::now();
    const long long a = sumByValue(values);
    const auto endValue = chrono::high_resolution_clock::now();

    const auto startRef = chrono::high_resolution_clock::now();
    const long long b = sumByConstRef(values);
    const auto endRef = chrono::high_resolution_clock::now();

    (void)a;
    (void)b;

    const auto valueTime =
        chrono::duration_cast<chrono::microseconds>(endValue - startValue).count();
    const auto refTime = chrono::duration_cast<chrono::microseconds>(endRef - startRef).count();

    cout << "By value (us): " << valueTime << '\n';
    cout << "By const ref (us): " << refTime << '\n';

    return 0;
}
