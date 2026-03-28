// This example demonstrates smart pointers in depth concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <iostream>
#include <memory>
#include <string>
using namespace std;

class Document {
  public:
    explicit Document(const string& nameValue) : name(nameValue) {
        // Intent: print intermediate or final output for quick behavior verification.
        cout << "Created: " << name << '\n';
    }

    ~Document() { cout << "Destroyed: " << name << '\n'; }

  private:
    string name;
};

int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    unique_ptr<Document> owner(new Document("DesignDoc"));

    shared_ptr<Document> teamA(new Document("SharedSpec"));
    shared_ptr<Document> teamB = teamA;
    weak_ptr<Document> observer = teamA;

    cout << "Shared use count: " << teamA.use_count() << '\n';

    // Intent: guard invalid or edge-case paths before the main path continues.
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
