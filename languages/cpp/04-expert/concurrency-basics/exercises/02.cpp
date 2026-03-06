#include <iostream>
#include <queue>
#include <string>

int main() {
    std::queue<int> q;

    std::cout << "Enter commands: produce <x>, consume, stop\n";
    while (true) {
        std::string command;
        std::cin >> command;

        if (!std::cin) {
            break;
        }

        if (command == "produce") {
            int value = 0;
            std::cin >> value;
            q.push(value);
            std::cout << "Produced " << value << ", size=" << q.size() << '\n';
        } else if (command == "consume") {
            if (q.empty()) {
                std::cout << "Queue is empty.\n";
            } else {
                std::cout << "Consumed " << q.front() << '\n';
                q.pop();
            }
        } else if (command == "stop") {
            break;
        } else {
            std::cout << "Unknown command.\n";
        }
    }

    return 0;
}
