#include <chrono>
#include <iostream>
#include <vector>
using namespace std;


int main() {
    int n = 0;
    cout << "How many push operations? ";
    cin >> n;

    if (n < 0) {
        cout << "Please enter a non-negative count.\n";
        return 0;
    }

    vector<int> withoutReserve;
    const auto startA = chrono::high_resolution_clock::now();
    for (int i = 0; i < n; ++i) {
        withoutReserve.push_back(i);
    }
    const auto endA = chrono::high_resolution_clock::now();

    vector<int> withReserve;
    withReserve.reserve(static_cast<size_t>(n));
    const auto startB = chrono::high_resolution_clock::now();
    for (int i = 0; i < n; ++i) {
        withReserve.push_back(i);
    }
    const auto endB = chrono::high_resolution_clock::now();

    const auto timeA = chrono::duration_cast<chrono::microseconds>(endA - startA).count();
    const auto timeB = chrono::duration_cast<chrono::microseconds>(endB - startB).count();

    cout << "Without reserve (us): " << timeA << '\n';
    cout << "With reserve (us): " << timeB << '\n';

    return 0;
}
