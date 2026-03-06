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
