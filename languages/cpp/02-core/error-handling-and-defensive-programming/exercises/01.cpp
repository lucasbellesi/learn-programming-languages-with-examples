/*
Exercise Guide: languages/cpp/02-core/error-handling-and-defensive-programming/exercises/01.cpp
Goal: Solve the task defined in this module's README Exercise Specs.
Build: g++ -std=c++17 -Wall -Wextra -pedantic languages/cpp/02-core/error-handling-and-defensive-programming/exercises/01.cpp -o 01_exercise
Run: ./01_exercise (Windows MSYS2: ./01_exercise.exe)
Sample Input: Use one of the sample cases from the module README Exercise Specs.
Expected Output: Follow the exact output rules described in the same exercise spec.
*/
#include <iostream>
#include <string>
using namespace std;


int main() {
    string row;
    cout << "Enter row (name,age,city): ";
    getline(cin, row);

    const size_t firstComma = row.find(',');
    if (firstComma == string::npos) {
        cout << "Invalid format. Missing commas.\n";
        return 0;
    }

    const size_t secondComma = row.find(',', firstComma + 1);
    if (secondComma == string::npos) {
        cout << "Invalid format. Missing second comma.\n";
        return 0;
    }

    const string name = row.substr(0, firstComma);
    const string age = row.substr(firstComma + 1, secondComma - firstComma - 1);
    const string city = row.substr(secondComma + 1);

    if (name.empty() || age.empty() || city.empty()) {
        cout << "Invalid format. Empty field detected.\n";
        return 0;
    }

    cout << "Name: " << name << '\n';
    cout << "Age: " << age << '\n';
    cout << "City: " << city << '\n';

    return 0;
}
