// Module focus: Modeling related data and behavior with structured types.
// Why it matters: the example makes it possible to model data and behavior with cohesive domain
// types before the learner tackles the exercises.

#include <iostream>
#include <string>
using namespace std;

struct Student {
    // A struct is a good fit for simple public data.
    string name;
    double grade;
};

class BankAccount {
  public:
    BankAccount(const string& ownerName, double initialBalance)
        : owner(ownerName), balance(initialBalance < 0.0 ? 0.0 : initialBalance) {}

    bool applyTransaction(double amount) {
        // A class can guard updates before private state changes.
        if (balance + amount < 0.0) {
            return false;
        }
        balance += amount;
        return true;
    }

    void print() const { cout << "Owner: " << owner << "\nBalance: " << balance << '\n'; }

  private:
    string owner;
    double balance;
};

// Fixed inputs make the consequence of exposing mutable state publicly without reason visible and
// repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    Student first{"Alex Johnson", 8.7};
    Student second{"Maya Patel", 9.1};

    // The printed result shows whether the program can protect invariants through constructors
    // and methods.
    cout << "Students (struct example):\n";
    cout << "Student{name=\"" << first.name << "\", grade=" << first.grade << "}\n";
    cout << "Student{name=\"" << second.name << "\", grade=" << second.grade << "}\n";

    BankAccount account("Alex Johnson", 100.0);
    account.applyTransaction(40.0);
    account.applyTransaction(-25.0);

    cout << "\nBank account (class example):\n";
    account.print();

    return 0;
}
