#include <iostream>
#include <string>
using namespace std;

class CounterGuard {
  public:
    explicit CounterGuard(int& sharedCounterRef, const string& labelText)
        : sharedCounter(sharedCounterRef), label(labelText) {
        ++sharedCounter;
        cout << "[enter] " << label << " | active guards: " << sharedCounter << '\n';
    }

    ~CounterGuard() {
        --sharedCounter;
        cout << "[exit]  " << label << " | active guards: " << sharedCounter << '\n';
    }

  private:
    int& sharedCounter;
    string label;
};

int main() {
    int activeGuards = 0;

    cout << "Starting scope demo.\n";
    {
        CounterGuard first(activeGuards, "first scope");
        {
            CounterGuard second(activeGuards, "nested scope");
            cout << "Inside nested scope.\n";
        }
        cout << "Back to first scope.\n";
    }

    cout << "Final active guards: " << activeGuards << '\n';
    return 0;
}
