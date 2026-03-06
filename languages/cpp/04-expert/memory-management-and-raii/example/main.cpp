#include <cstddef>
#include <iostream>
#include <memory>
#include <string>

class ScopedMessage {
public:
    explicit ScopedMessage(const std::string& labelText) : label(labelText) {
        std::cout << "[acquire] " << label << '\n';
    }

    ~ScopedMessage() {
        std::cout << "[release] " << label << '\n';
    }

private:
    std::string label;
};

std::unique_ptr<int[]> makeSequence(std::size_t size) {
    std::unique_ptr<int[]> data(new int[size]);
    for (std::size_t i = 0; i < size; ++i) {
        data[i] = static_cast<int>((i + 1) * 10);
    }
    return data;
}

void printSequence(const std::unique_ptr<int[]>& data, std::size_t size) {
    std::cout << "Sequence: ";
    for (std::size_t i = 0; i < size; ++i) {
        std::cout << data[i];
        if (i + 1 < size) {
            std::cout << ' ';
        }
    }
    std::cout << '\n';
}

int main() {
    std::cout << "RAII scope demo:\n";
    {
        ScopedMessage scoped("temporary operation");
        std::cout << "Inside scope.\n";
    }

    const std::size_t size = 5;
    std::unique_ptr<int[]> values = makeSequence(size);
    printSequence(values, size);

    std::cout << "Ownership transfer with move:\n";
    std::unique_ptr<int[]> movedValues = std::move(values);
    if (!values) {
        std::cout << "Original pointer is now empty after move.\n";
    }
    printSequence(movedValues, size);

    return 0;
}
