#include <iostream>

using namespace std;

int main() {
    int choice = 0;
    int sum = 0;
    int number = 0;

    while (true) {
        cout << "\nMenu\n";
        cout << "1) Add number to sum\n";
        cout << "2) Show current sum\n";
        cout << "3) Reset sum\n";
        cout << "4) Exit\n";
        cout << "Choose an option: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter a number: ";
                cin >> number;
                sum += number;
                cout << "Added. New sum is " << sum << ".\n";
                break;
            case 2:
                cout << "Current sum: " << sum << '\n';
                break;
            case 3:
                sum = 0;
                cout << "Sum reset to 0.\n";
                break;
            case 4:
                cout << "Goodbye.\n";
                return 0;
            default:
                cout << "Invalid option. Try again.\n";
                break;
        }
    }
}
