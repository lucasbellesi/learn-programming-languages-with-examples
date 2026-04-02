// This example shows tying resource cleanup to object lifetime so cleanup stays predictable.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <cstddef>
#include <iostream>
#include <memory>
#include <string>
using namespace std;

class ScopedMessage {
  public:
    explicit ScopedMessage(const string& labelText) : label(labelText) {
        cout << "[acquire] " << label << '\n';
    }

    ~ScopedMessage() { cout << "[release] " << label << '\n'; }

  private:
    string label;
};

// Define the reusable pieces first so the main flow can focus on one observable scenario.
unique_ptr<int[]> makeSequence(size_t size) {
    unique_ptr<int[]> data(new int[size]);
    for (size_t i = 0; i < size; ++i) {
        data[i] = static_cast<int>((i + 1) * 10);
    }
    return data;
}

void printSequence(const unique_ptr<int[]>& data, size_t size) {
    cout << "Sequence: ";
    for (size_t i = 0; i < size; ++i) {
        cout << data[i];
        if (i + 1 < size) {
            cout << ' ';
        }
    }
    cout << '\n';
}

// Run one deterministic scenario so the console output makes tying resource cleanup to object
// lifetime so cleanup stays predictable easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    // Print the observed state here so learners can connect the code path to a concrete result.
    cout << "RAII scope demo:\n";
    {
        ScopedMessage scoped("temporary operation");
        cout << "Inside scope.\n";
    }

    const size_t size = 5;
    unique_ptr<int[]> values = makeSequence(size);
    printSequence(values, size);

    cout << "Ownership transfer with move:\n";
    unique_ptr<int[]> movedValues = move(values);
    if (!values) {
        cout << "Original pointer is now empty after move.\n";
    }
    printSequence(movedValues, size);

    return 0;
}
