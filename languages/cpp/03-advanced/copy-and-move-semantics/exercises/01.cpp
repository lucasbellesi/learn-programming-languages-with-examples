#include <iostream>
#include <utility>
#include <vector>
using namespace std;


class IntBuffer {
public:
    explicit IntBuffer(size_t size) : data(size, 0) {
        cout << "Constructed IntBuffer\n";
    }

    IntBuffer(const IntBuffer& other) : data(other.data) {
        cout << "Copied IntBuffer\n";
    }

    IntBuffer(IntBuffer&& other) noexcept : data(move(other.data)) {
        cout << "Moved IntBuffer\n";
    }

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

private:
    vector<int> data;
};

int main() {
    IntBuffer a(4);
    IntBuffer b = a;
    IntBuffer c = move(a);
    b = c;
    c = move(b);
    return 0;
}
