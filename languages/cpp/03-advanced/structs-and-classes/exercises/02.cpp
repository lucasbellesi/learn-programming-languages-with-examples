#include <iostream>
#include <limits>
#include <string>
using namespace std;


class Counter {
public:
    Counter() : value(0) {}

    void increment() {
        ++value;
    }

    void decrement() {
        --value;
    }

    void reset() {
        value = 0;
    }

    int getValue() const {
        return value;
    }

private:
    int value;
};

int main() {
    Counter counter;
    string command;

    cout << "Commands: inc, dec, reset, stop\n";
    while (true) {
        cout << "Enter command: ";
        if (!(cin >> command)) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        if (command == "inc") {
            counter.increment();
        } else if (command == "dec") {
            counter.decrement();
        } else if (command == "reset") {
            counter.reset();
        } else if (command == "stop") {
            break;
        } else {
            cout << "Unknown command.\n";
            continue;
        }

        cout << "Current value: " << counter.getValue() << '\n';
    }

    cout << "Final value: " << counter.getValue() << '\n';
    return 0;
}
