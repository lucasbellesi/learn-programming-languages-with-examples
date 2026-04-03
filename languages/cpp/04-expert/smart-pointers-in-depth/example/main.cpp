// Module focus: Tracking ownership and lifetime when multiple references can observe the same
// value. Why it matters: practicing smart pointers in depth patterns makes exercises and
// checkpoints easier to reason about.

// This example shows tracking ownership and lifetime when multiple references can observe the same
// value. In C++, the example keeps value flow, references, and explicit control visible.

#include <iostream>
#include <memory>
#include <string>
using namespace std;

class Document {
  public:
    explicit Document(const string& nameValue) : name(nameValue) {
        cout << "Created: " << name << '\n';
    }

    ~Document() { cout << "Destroyed: " << name << '\n'; }

  private:
    string name;
};

// Walk through one fixed scenario so smart pointers in depth behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key smart pointers in depth path.
    unique_ptr<Document> owner(new Document("DesignDoc"));

    shared_ptr<Document> teamA(new Document("SharedSpec"));
    shared_ptr<Document> teamB = teamA;
    weak_ptr<Document> observer = teamA;

    // Report values so learners can verify the smart pointers in depth outcome.
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
