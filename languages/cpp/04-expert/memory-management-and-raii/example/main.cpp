// This example demonstrates memory management and raii concepts.

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

    ~ScopedMessage() {
        cout << "[release] " << label << '\n';
    }

private:
    string label;
};

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

int main() {
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
