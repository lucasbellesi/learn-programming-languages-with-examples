#include <condition_variable>
#include <iostream>
#include <mutex>
#include <queue>
#include <thread>
using namespace std;


int main() {
    int itemsToProduce = 0;
    cout << "How many items should be produced? ";
    cin >> itemsToProduce;

    if (itemsToProduce < 0) {
        cout << "Please enter a non-negative value.\n";
        return 0;
    }

    queue<int> queue;
    mutex queueMutex;
    condition_variable queueCv;
    bool productionFinished = false;
    int consumedCount = 0;

    thread producer([&]() {
        for (int i = 1; i <= itemsToProduce; ++i) {
            {
                lock_guard<mutex> lock(queueMutex);
                queue.push(i);
                cout << "Produced: " << i << '\n';
            }
            queueCv.notify_one();
        }

        {
            lock_guard<mutex> lock(queueMutex);
            productionFinished = true;
        }
        queueCv.notify_one();
    });

    thread consumer([&]() {
        while (true) {
            unique_lock<mutex> lock(queueMutex);
            queueCv.wait(lock, [&]() { return productionFinished || !queue.empty(); });

            if (queue.empty() && productionFinished) {
                break;
            }

            const int value = queue.front();
            queue.pop();
            ++consumedCount;
            cout << "Consumed: " << value << '\n';
        }
    });

    producer.join();
    consumer.join();

    cout << "Finished. Total consumed: " << consumedCount << '\n';
    return 0;
}
