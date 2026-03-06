#include <iostream>
#include <memory>

class Resource {
public:
    Resource() {
        std::cout << "Resource acquired\n";
    }

    ~Resource() {
        std::cout << "Resource released\n";
    }
};

int main() {
    std::unique_ptr<Resource> resource(new Resource());

    std::unique_ptr<Resource> moved = std::move(resource);
    if (!resource) {
        std::cout << "Ownership moved successfully.\n";
    }

    if (moved) {
        std::cout << "Moved owner is active.\n";
    }

    return 0;
}
