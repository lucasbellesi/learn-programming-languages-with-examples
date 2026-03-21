// This example demonstrates copy and move semantics concepts.

#include <iostream>
#include <utility>
#include <vector>
using namespace std;


class Buffer {
public:
    explicit Buffer(size_t size) : data(size, 0) {
        cout << "Constructed\n";
    }

    Buffer(const Buffer& other) : data(other.data) {
        cout << "Copied\n";
    }

    Buffer(Buffer&& other) noexcept : data(move(other.data)) {
        cout << "Moved\n";
    }

    Buffer& operator=(const Buffer& other) {
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
    Buffer first(3);
    Buffer second = first;
    Buffer third = makeBuffer();

    second = move(third);

    cout << "second size: " << second.size() << '\n';
    return 0;
}
