#include <iostream>
#include <memory>
#include <string>
using namespace std;


class Document {
public:
    explicit Document(const string& nameValue) : name(nameValue) {
        cout << "Created: " << name << '\n';
    }

    ~Document() {
        cout << "Destroyed: " << name << '\n';
    }

private:
    string name;
};

int main() {
    unique_ptr<Document> owner(new Document("DesignDoc"));

    shared_ptr<Document> teamA(new Document("SharedSpec"));
    shared_ptr<Document> teamB = teamA;
    weak_ptr<Document> observer = teamA;

    cout << "Shared use count: " << teamA.use_count() << '\n';

    if (shared_ptr<Document> locked = observer.lock()) {
        cout << "Observer can access shared document.\n";
        (void)locked;
    }

    owner.reset();
    teamA.reset();
    teamB.reset();

    if (observer.expired()) {
        cout << "Observer is expired after shared owners released.\n";
    }

    return 0;
}
