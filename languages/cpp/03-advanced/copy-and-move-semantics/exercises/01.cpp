#include <iostream>
#include <utility>
#include <vector>

class IntBuffer {
public:
    explicit IntBuffer(std::size_t size) : data(size, 0) {
        std::cout << "Constructed IntBuffer\n";
    }

    IntBuffer(const IntBuffer& other) : data(other.data) {
        std::cout << "Copied IntBuffer\n";
    }

    IntBuffer(IntBuffer&& other) noexcept : data(std::move(other.data)) {
        std::cout << "Moved IntBuffer\n";
    }

    IntBuffer& operator=(const IntBuffer& other) {
        if (this != &other) {
            data = other.data;
            std::cout << "Copy-assigned IntBuffer\n";
        }
        return *this;
    }

    IntBuffer& operator=(IntBuffer&& other) noexcept {
        if (this != &other) {
            data = std::move(other.data);
            std::cout << "Move-assigned IntBuffer\n";
        }
        return *this;
    }

private:
    std::vector<int> data;
};

int main() {
    IntBuffer a(4);
    IntBuffer b = a;
    IntBuffer c = std::move(a);
    b = c;
    c = std::move(b);
    return 0;
}
