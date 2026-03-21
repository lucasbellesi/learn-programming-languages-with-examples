// This example demonstrates memory management and raii concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <cstddef>
#include <iostream>
#include <memory>
#include <string>
using namespace std;


class ScopedMessage {
public:
    explicit ScopedMessage(const string& labelText) : label(labelText) {
        // Intent: print intermediate or final output for quick behavior verification.
        cout << "[acquire] " << label << '\n';
    }

    ~ScopedMessage() {
        cout << "[release] " << label << '\n';
    }

private:
    string label;
};

unique_ptr<int[]> makeSequence(size_t size) {
    unique_ptr<int[]> data(new int[size]);
    // Intent: iterate through data in a clear and deterministic order.
    for (size_t i = 0; i < size; ++i) {
        data[i] = static_cast<int>((i + 1) * 10);
    }
    return data;
}

void printSequence(const unique_ptr<int[]>& data, size_t size) {
    cout << "Sequence: ";
    for (size_t i = 0; i < size; ++i) {
        cout << data[i];
        // Intent: guard invalid or edge-case paths before the main path continues.
        if (i + 1 < size) {
            cout << ' ';
        }
    }
    cout << '\n';
}

int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
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
