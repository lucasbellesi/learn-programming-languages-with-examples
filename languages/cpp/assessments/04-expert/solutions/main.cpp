#include <algorithm>
#include <iostream>
#include <limits>
#include <memory>
#include <mutex>
#include <thread>
#include <vector>

using namespace std;

struct Summary {
    long long total = 0;
    int minimum = numeric_limits<int>::max();
    int maximum = numeric_limits<int>::min();
};

int main() {
    auto data = make_unique<vector<int>>(vector<int>{12, 7, 25, 4, 31, 19, 2, 45, 18, 9, 27, 6});

    const size_t threadCount = 3;
    vector<thread> workers;
    workers.reserve(threadCount);

    Summary globalSummary;
    mutex summaryMutex;

    const size_t chunkSize = (data->size() + threadCount - 1) / threadCount;

    for (size_t workerId = 0; workerId < threadCount; ++workerId) {
        const size_t begin = workerId * chunkSize;
        const size_t end = min(begin + chunkSize, data->size());

        workers.emplace_back([workerId, begin, end, &data, &globalSummary, &summaryMutex]() {
            if (begin >= end) {
                return;
            }

            long long localTotal = 0;
            int localMin = (*data)[begin];
            int localMax = (*data)[begin];

            for (size_t i = begin; i < end; ++i) {
                const int value = (*data)[i];
                localTotal += value;
                if (value < localMin) {
                    localMin = value;
                }
                if (value > localMax) {
                    localMax = value;
                }
            }

            {
                lock_guard<mutex> lock(summaryMutex);
                cout << "Worker " << workerId << " partial sum: " << localTotal << '\n';
                globalSummary.total += localTotal;
                if (localMin < globalSummary.minimum) {
                    globalSummary.minimum = localMin;
                }
                if (localMax > globalSummary.maximum) {
                    globalSummary.maximum = localMax;
                }
            }
        });
    }

    for (thread& worker : workers) {
        worker.join();
    }

    cout << "\nFinal summary:\n";
    cout << "Total: " << globalSummary.total << '\n';
    cout << "Minimum: " << globalSummary.minimum << '\n';
    cout << "Maximum: " << globalSummary.maximum << '\n';

    return 0;
}
