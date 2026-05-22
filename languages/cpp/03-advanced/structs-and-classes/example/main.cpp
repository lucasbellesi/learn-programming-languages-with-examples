// Module focus: Modeling related data and behavior with structured types.
// Why it matters: practicing structs and classes patterns makes exercises and checkpoints easier to
// reason about.

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

// Walk through one fixed scenario so structs and classes behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key structs and classes path.
    Student first{"Alex Johnson", 8.7};
    Student second{"Maya Patel", 9.1};

    // Report values so learners can verify the structs and classes outcome.
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
