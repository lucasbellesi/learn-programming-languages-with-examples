#include <iostream>
#include <string>
#include <vector>

struct Student {
    std::string name;
    int age;
    double grade;

    void print() const {
        std::cout << "Student{name=\"" << name << "\", age=" << age
                  << ", grade=" << grade << "}\n";
    }
};

class BankAccount {
public:
    BankAccount(const std::string& ownerName, double initialBalance)
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

    const std::string& getOwner() const {
        return owner;
    }

    double getBalance() const {
        return balance;
    }

private:
    std::string owner;
    double balance;
};

int main() {
    std::vector<Student> students{
        {"Alex Johnson", 19, 8.7},
        {"Maya Patel", 20, 9.1}
    };

    std::cout << "Students (struct example):\n";
    for (const Student& student : students) {
        student.print();
    }

    BankAccount account("Alex Johnson", 100.0);
    account.deposit(40.0);
    account.withdraw(25.0);

    std::cout << "\nBank account (class example):\n";
    std::cout << "Owner: " << account.getOwner() << '\n';
    std::cout << "Balance: " << account.getBalance() << '\n';

    return 0;
}
