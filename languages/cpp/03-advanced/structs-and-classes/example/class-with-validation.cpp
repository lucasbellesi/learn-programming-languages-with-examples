#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

class BankAccount {
public:
    BankAccount(string ownerName, double initialBalance)
        : owner(ownerName), balance(0.0) {
        if (owner.empty()) {
            throw invalid_argument("Owner name cannot be empty.");
        }
        if (initialBalance < 0.0) {
            throw invalid_argument("Initial balance cannot be negative.");
        }
        balance = initialBalance;
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

    const string& getOwner() const {
        return owner;
    }

    double getBalance() const {
        return balance;
    }

private:
    string owner;
    double balance;
};

int main() {
    try {
        BankAccount account("Ana Smith", 100.0);

        cout << "Account owner: " << account.getOwner() << '\n';
        cout << "Initial balance: " << account.getBalance() << '\n';

        if (account.deposit(50.0)) {
            cout << "Deposit successful.\n";
        }

        if (account.withdraw(30.0)) {
            cout << "Withdraw successful.\n";
        }

        if (!account.withdraw(500.0)) {
            cout << "Withdraw rejected (insufficient funds).\n";
        }

        cout << "Final balance: " << account.getBalance() << '\n';
    } catch (const exception& ex) {
        cout << "Error: " << ex.what() << '\n';
    }

    return 0;
}
