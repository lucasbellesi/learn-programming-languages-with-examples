#include <iostream>
#include <utility>
#include <vector>

class Buffer {
public:
    explicit Buffer(std::size_t size) : data(size, 0) {
        std::cout << "Constructed\n";
    }

    Buffer(const Buffer& other) : data(other.data) {
        std::cout << "Copied\n";
    }

    Buffer(Buffer&& other) noexcept : data(std::move(other.data)) {
        std::cout << "Moved\n";
    }

    Buffer& operator=(const Buffer& other) {
        if (this != &other) {
            data = other.data;
            std::cout << "Copy-assigned\n";
        }
        return *this;
    }

    Buffer& operator=(Buffer&& other) noexcept {
        if (this != &other) {
            data = std::move(other.data);
            std::cout << "Move-assigned\n";
        }
        return *this;
    }

    std::size_t size() const {
        return data.size();
    }

private:
    std::vector<int> data;
};

Buffer makeBuffer() {
    Buffer b(5);
    return b;
}

int main() {
    Buffer first(3);
    Buffer second = first;
    Buffer third = makeBuffer();

    second = std::move(third);

    std::cout << "second size: " << second.size() << '\n';
    return 0;
}
