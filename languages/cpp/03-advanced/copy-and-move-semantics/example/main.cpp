// Module focus: How copying, sharing, or transferring state changes later behavior.
// Why it matters: the example makes it possible to predict aliasing and independence after
// copying or sharing values before the learner tackles the exercises.

#include <iostream>
#include <utility>
#include <vector>
using namespace std;

class Buffer {
  public:
    explicit Buffer(size_t size) : data(size, 0) { cout << "Constructed\n"; }

    Buffer(const Buffer& other) : data(other.data) { cout << "Copied\n"; }

    Buffer(Buffer&& other) noexcept : data(move(other.data)) { cout << "Moved\n"; }

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

    size_t size() const { return data.size(); }

  private:
    vector<int> data;
};

// Separate helpers keep the main path focused on how to predict aliasing and independence after
// copying or sharing values.
Buffer makeBuffer() {
    Buffer b(5);
    return b;
}

// Fixed inputs make the consequence of using moved-from objects without reinitialization visible
// and repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    Buffer first(3);
    Buffer second = first;
    Buffer third = makeBuffer();

    second = move(third);

    // The printed result shows whether the program can choose an idiomatic ownership-transfer
    // strategy for the language.
    cout << "second size: " << second.size() << '\n';
    return 0;
}
