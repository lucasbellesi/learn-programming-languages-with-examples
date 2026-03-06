#include <condition_variable>
#include <iostream>
#include <mutex>
#include <queue>
#include <thread>

int main() {
    int itemsToProduce = 0;
    std::cout << "How many items should be produced? ";
    std::cin >> itemsToProduce;

    if (itemsToProduce < 0) {
        std::cout << "Please enter a non-negative value.\n";
        return 0;
    }

    std::queue<int> queue;
    std::mutex queueMutex;
    std::condition_variable queueCv;
    bool productionFinished = false;
    int consumedCount = 0;

    std::thread producer([&]() {
        for (int i = 1; i <= itemsToProduce; ++i) {
            {
                std::lock_guard<std::mutex> lock(queueMutex);
                queue.push(i);
                std::cout << "Produced: " << i << '\n';
            }
            queueCv.notify_one();
        }

        {
            std::lock_guard<std::mutex> lock(queueMutex);
            productionFinished = true;
        }
        queueCv.notify_one();
    });

    std::thread consumer([&]() {
        while (true) {
            std::unique_lock<std::mutex> lock(queueMutex);
            queueCv.wait(lock, [&]() { return productionFinished || !queue.empty(); });

            if (queue.empty() && productionFinished) {
                break;
            }

            const int value = queue.front();
            queue.pop();
            ++consumedCount;
            std::cout << "Consumed: " << value << '\n';
        }
    });

    producer.join();
    consumer.join();

    std::cout << "Finished. Total consumed: " << consumedCount << '\n';
    return 0;
}
