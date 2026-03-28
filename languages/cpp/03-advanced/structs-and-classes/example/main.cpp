// This example demonstrates structs and classes concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Student {
    string name;
    int age;
    double grade;

    void print() const {
        // Intent: print intermediate or final output for quick behavior verification.
        cout << "Student{name=\"" << name << "\", age=" << age << ", grade=" << grade << "}\n";
    }
};

class BankAccount {
  public:
    BankAccount(const string& ownerName, double initialBalance)
        : owner(ownerName), balance(initialBalance) {
        // Intent: guard invalid or edge-case paths before the main path continues.
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

int main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    vector<Student> students{{"Alex Johnson", 19, 8.7}, {"Maya Patel", 20, 9.1}};

    cout << "Students (struct example):\n";
    // Intent: iterate through data in a clear and deterministic order.
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
