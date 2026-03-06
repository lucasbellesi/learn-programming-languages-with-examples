#include <iostream>
#include <limits>
#include <string>

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
    std::string command;

    std::cout << "Commands: inc, dec, reset, stop\n";
    while (true) {
        std::cout << "Enter command: ";
        if (!(std::cin >> command)) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
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
            std::cout << "Unknown command.\n";
            continue;
        }

        std::cout << "Current value: " << counter.getValue() << '\n';
    }

    std::cout << "Final value: " << counter.getValue() << '\n';
    return 0;
}
