#include <iostream>
#include <string>

class Course {
  public:
    Course(const std::string& titleValue, int capacityValue)
        : title(titleValue), capacity(capacityValue), enrolled(0) {
        if (capacity < 0) {
            capacity = 0;
        }
    }

    bool enroll() {
        if (enrolled >= capacity) {
            return false;
        }
        ++enrolled;
        return true;
    }

    bool drop() {
        if (enrolled <= 0) {
            return false;
        }
        --enrolled;
        return true;
    }

    void printStatus() const {
        std::cout << "Course: " << title << " | " << enrolled << "/" << capacity << " enrolled\n";
    }

  private:
    std::string title;
    int capacity;
    int enrolled;
};

int main() {
    Course cppBasics("CppBasics", 2);
    Course algorithms("Algorithms", 3);

    cppBasics.enroll();
    cppBasics.enroll();
    cppBasics.enroll();

    algorithms.enroll();

    cppBasics.printStatus();
    algorithms.printStatus();

    return 0;
}
