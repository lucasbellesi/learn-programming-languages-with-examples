#include <iostream>
#include <memory>

class Parent;

class Child {
public:
    void setParent(const std::shared_ptr<Parent>& parentRef) {
        parent = parentRef;
    }

    void checkParent() const {
        if (parent.lock()) {
            std::cout << "Parent is still alive.\n";
        } else {
            std::cout << "Parent no longer exists.\n";
        }
    }

private:
    std::weak_ptr<Parent> parent;
};

class Parent : public std::enable_shared_from_this<Parent> {
public:
    void attachChild(const std::shared_ptr<Child>& child) {
        childRef = child;
        child->setParent(shared_from_this());
    }

private:
    std::shared_ptr<Child> childRef;
};

int main() {
    std::shared_ptr<Child> child(new Child());

    {
        std::shared_ptr<Parent> parent(new Parent());
        parent->attachChild(child);
        child->checkParent();
    }

    child->checkParent();
    return 0;
}
