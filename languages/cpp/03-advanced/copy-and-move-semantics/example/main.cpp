// Module focus: How copying, sharing, or transferring state changes later behavior.
// Why it matters: practicing copy and move semantics patterns makes exercises and checkpoints
// easier to reason about.

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

// Helper setup for copy and move semantics; this keeps the walkthrough readable.
Buffer makeBuffer() {
    Buffer b(5);
    return b;
}

// Walk through one fixed scenario so copy and move semantics behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key copy and move semantics path.
    Buffer first(3);
    Buffer second = first;
    Buffer third = makeBuffer();

    second = move(third);

    // Report values so learners can verify the copy and move semantics outcome.
    cout << "second size: " << second.size() << '\n';
    return 0;
}
