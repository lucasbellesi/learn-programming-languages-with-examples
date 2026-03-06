#include <iostream>
#include <memory>
using namespace std;


class Resource {
public:
    Resource() {
        cout << "Resource acquired\n";
    }

    ~Resource() {
        cout << "Resource released\n";
    }
};

int main() {
    unique_ptr<Resource> resource(new Resource());

    unique_ptr<Resource> moved = move(resource);
    if (!resource) {
        cout << "Ownership moved successfully.\n";
    }

    if (moved) {
        cout << "Moved owner is active.\n";
    }

    return 0;
}
