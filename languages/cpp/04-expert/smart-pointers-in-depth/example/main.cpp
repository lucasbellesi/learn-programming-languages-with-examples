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

// Run one deterministic scenario so the console output makes tracking ownership and lifetime when
// multiple references can observe the same value easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    unique_ptr<Document> owner(new Document("DesignDoc"));

    shared_ptr<Document> teamA(new Document("SharedSpec"));
    shared_ptr<Document> teamB = teamA;
    weak_ptr<Document> observer = teamA;

    // Print the observed state here so learners can connect the code path to a concrete result.
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
