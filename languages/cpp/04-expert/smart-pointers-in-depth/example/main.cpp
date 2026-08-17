// Module focus: Tracking ownership and lifetime when multiple references can observe the same
// value. Why it matters: the example makes it possible to model exclusive, shared, and non-owning
// relationships idiomatically before the learner tackles the exercises.

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

// Fixed inputs make the consequence of overusing `shared_ptr` where `unique_ptr` is sufficient
// visible and repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    unique_ptr<Document> owner(new Document("DesignDoc"));

    shared_ptr<Document> teamA(new Document("SharedSpec"));
    shared_ptr<Document> teamB = teamA;
    weak_ptr<Document> observer = teamA;

    // The printed result shows whether the program can prevent leaks, cycles, and stale
    // observations in ownership graphs.
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
