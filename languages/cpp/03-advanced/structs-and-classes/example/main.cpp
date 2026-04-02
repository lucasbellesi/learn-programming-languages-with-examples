// This example shows modeling related data and behavior with structured types.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Student {
    string name;
    int age;
    double grade;

    void print() const {
        cout << "Student{name=\"" << name << "\", age=" << age << ", grade=" << grade << "}\n";
    }
};

class BankAccount {
  public:
    BankAccount(const string& ownerName, double initialBalance)
        : owner(ownerName), balance(initialBalance) {
        if (balance < 0.0) {
            balance = 0.0;
        }
    }

    bool deposit(double amount) {
        if (amount <= 0.0) {
            return false;
        }
        balance += amount;
        return true;
    }

    bool withdraw(double amount) {
        if (amount <= 0.0 || amount > balance) {
            return false;
        }
        balance -= amount;
        return true;
    }

    const string& getOwner() const { return owner; }

    double getBalance() const { return balance; }

  private:
    string owner;
    double balance;
};

// Run one deterministic scenario so the console output makes modeling related data and behavior
// with structured types easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    vector<Student> students{{"Alex Johnson", 19, 8.7}, {"Maya Patel", 20, 9.1}};

    // Print the observed state here so learners can connect the code path to a concrete result.
    cout << "Students (struct example):\n";
    for (const Student& student : students) {
        student.print();
    }

    BankAccount account("Alex Johnson", 100.0);
    account.deposit(40.0);
    account.withdraw(25.0);

    cout << "\nBank account (class example):\n";
    cout << "Owner: " << account.getOwner() << '\n';
    cout << "Balance: " << account.getBalance() << '\n';

    return 0;
}
