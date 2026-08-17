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

void runNestedScopes(int depth, int level, int& activeGuards) {
    if (level > depth) {
        cout << "Inside deepest scope | active guards: " << activeGuards << '\n';
        return;
    }

    CounterGuard guard(activeGuards, "scope " + to_string(level));
    runNestedScopes(depth, level + 1, activeGuards);
}

int main() {
    int depth = 0;
    if (!(cin >> depth) || depth <= 0) {
        cout << "Depth must be positive.\n";
        return 0;
    }
    int activeGuards = 0;

    cout << "Starting scope demo.\n";
    runNestedScopes(depth, 1, activeGuards);

    cout << "Final active guards: " << activeGuards << '\n';
    return 0;
}
