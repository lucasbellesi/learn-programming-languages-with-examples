// Module focus: Modeling related data and behavior with structured types.
// Why it matters: practicing structs and classes patterns makes exercises and checkpoints easier to
// reason about.

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

// Walk through one fixed scenario so structs and classes behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key structs and classes path.
    vector<Student> students{{"Alex Johnson", 19, 8.7}, {"Maya Patel", 20, 9.1}};

    // Report values so learners can verify the structs and classes outcome.
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
