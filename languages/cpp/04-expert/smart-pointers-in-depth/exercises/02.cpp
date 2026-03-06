#include <iostream>
#include <memory>
using namespace std;


class Parent;

class Child {
public:
    void setParent(const shared_ptr<Parent>& parentRef) {
        parent = parentRef;
    }

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
    shared_ptr<Child> child(new Child());

    {
        shared_ptr<Parent> parent(new Parent());
        parent->attachChild(child);
        child->checkParent();
    }

    child->checkParent();
    return 0;
}
