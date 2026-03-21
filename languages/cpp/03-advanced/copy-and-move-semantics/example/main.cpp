// This example demonstrates copy and move semantics concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <iostream>
#include <utility>
#include <vector>
using namespace std;


class Buffer {
public:
    explicit Buffer(size_t size) : data(size, 0) {
        // Intent: print intermediate or final output for quick behavior verification.
        cout << "Constructed\n";
    }

    Buffer(const Buffer& other) : data(other.data) {
        cout << "Copied\n";
    }

    Buffer(Buffer&& other) noexcept : data(move(other.data)) {
        cout << "Moved\n";
    }

    Buffer& operator=(const Buffer& other) {
        // Intent: guard invalid or edge-case paths before the main path continues.
        if (this != &other) {
            data = other.data;
            cout << "Copy-assigned\n";
        }
        return *this;
    }

    Buffer& operator=(Buffer&& other) noexcept {
        if (this != &other) {
            data = move(other.data);
            cout << "Move-assigned\n";
        }
        return *this;
    }

    size_t size() const {
        return data.size();
    }

private:
    vector<int> data;
};

Buffer makeBuffer() {
    Buffer b(5);
    return b;
}

int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    Buffer first(3);
    Buffer second = first;
    Buffer third = makeBuffer();

    second = move(third);

    cout << "second size: " << second.size() << '\n';
    return 0;
}
