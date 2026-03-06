#include <iostream>
#include <memory>
#include <string>

class Document {
public:
    explicit Document(const std::string& nameValue) : name(nameValue) {
        std::cout << "Created: " << name << '\n';
    }

    ~Document() {
        std::cout << "Destroyed: " << name << '\n';
    }

private:
    std::string name;
};

int main() {
    std::unique_ptr<Document> owner(new Document("DesignDoc"));

    std::shared_ptr<Document> teamA(new Document("SharedSpec"));
    std::shared_ptr<Document> teamB = teamA;
    std::weak_ptr<Document> observer = teamA;

    std::cout << "Shared use count: " << teamA.use_count() << '\n';

    if (std::shared_ptr<Document> locked = observer.lock()) {
        std::cout << "Observer can access shared document.\n";
        (void)locked;
    }

    owner.reset();
    teamA.reset();
    teamB.reset();

    if (observer.expired()) {
        std::cout << "Observer is expired after shared owners released.\n";
    }

    return 0;
}
