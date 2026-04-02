// This example shows how copying, sharing, or transferring state changes later behavior.
// In C++, the example keeps value flow, references, and explicit control visible.

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

// Define the reusable pieces first so the main flow can focus on one observable scenario.
Buffer makeBuffer() {
    Buffer b(5);
    return b;
}

// Run one deterministic scenario so the console output makes how copying, sharing, or transferring
// state changes later behavior easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    Buffer first(3);
    Buffer second = first;
    Buffer third = makeBuffer();

    second = move(third);

    // Print the observed state here so learners can connect the code path to a concrete result.
    cout << "second size: " << second.size() << '\n';
    return 0;
}
