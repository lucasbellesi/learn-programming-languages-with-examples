#include <iostream>
#include <memory>
#include <string>
using namespace std;

class Parent;

class Child {
  public:
    void setParent(const shared_ptr<Parent>& parentRef) { parent = parentRef; }

    void checkParent() const {
        if (parent.lock()) {
            cout << "Parent is still alive.\n";
        } else {
            cout << "Parent no longer exists.\n";
        }
    }

  private:
    weak_ptr<Parent> parent;
};

class Parent : public enable_shared_from_this<Parent> {
  public:
    void attachChild(const shared_ptr<Child>& child) {
        childRef = child;
        child->setParent(shared_from_this());
    }

  private:
    shared_ptr<Child> childRef;
};

int main() {
    string scenario;
    cin >> scenario;
    shared_ptr<Child> child(new Child());

    if (scenario == "missing") {
        child->checkParent();
        return 0;
    }

    {
        shared_ptr<Parent> parent(new Parent());
        parent->attachChild(child);
        if (scenario == "alive") {
            child->checkParent();
            return 0;
        }
    }

    child->checkParent();
    return 0;
}
