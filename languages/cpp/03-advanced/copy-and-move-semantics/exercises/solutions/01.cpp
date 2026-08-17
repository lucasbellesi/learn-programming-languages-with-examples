#include <iostream>
#include <utility>
#include <vector>
using namespace std;

class IntBuffer {
  public:
    explicit IntBuffer(size_t size) : data(size, 0) { cout << "Constructed IntBuffer\n"; }

    IntBuffer(const IntBuffer& other) : data(other.data) { cout << "Copied IntBuffer\n"; }

    IntBuffer(IntBuffer&& other) noexcept : data(move(other.data)) { cout << "Moved IntBuffer\n"; }

    IntBuffer& operator=(const IntBuffer& other) {
        if (this != &other) {
            data = other.data;
            cout << "Copy-assigned IntBuffer\n";
        }
        return *this;
    }

    IntBuffer& operator=(IntBuffer&& other) noexcept {
        if (this != &other) {
            data = move(other.data);
            cout << "Move-assigned IntBuffer\n";
        }
        return *this;
    }

    size_t size() const { return data.size(); }

  private:
    vector<int> data;
};

int main() {
    size_t size = 0;
    bool testSelfAssignment = false;
    if (!(cin >> size >> testSelfAssignment)) {
        cout << "Expected: size selfAssignmentFlag\n";
        return 0;
    }

    IntBuffer a(size);
    IntBuffer b = a;
    IntBuffer c = move(a);
    b = c;
    c = move(b);

    if (testSelfAssignment) {
        b = b;
        IntBuffer* sameBuffer = &c;
        c = move(*sameBuffer);
        cout << "Self-assignment preserved: " << c.size() << '\n';
    }
    cout << "Final sizes: " << a.size() << ' ' << b.size() << ' ' << c.size() << '\n';
    return 0;
}
