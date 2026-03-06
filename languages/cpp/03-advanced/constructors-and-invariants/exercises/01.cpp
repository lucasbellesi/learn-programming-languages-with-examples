#include <iostream>

class BankAccount {
public:
    explicit BankAccount(double initialBalance) : balance(initialBalance) {
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

    double getBalance() const {
        return balance;
    }

private:
    double balance;
};

int main() {
    double initial = 0.0;
    std::cout << "Initial balance: ";
    std::cin >> initial;

    BankAccount account(initial);

    double depositAmount = 0.0;
    std::cout << "Deposit amount: ";
    std::cin >> depositAmount;
    account.deposit(depositAmount);

    double withdrawAmount = 0.0;
    std::cout << "Withdraw amount: ";
    std::cin >> withdrawAmount;
    if (!account.withdraw(withdrawAmount)) {
        std::cout << "Withdrawal rejected.\n";
    }

    std::cout << "Final balance: " << account.getBalance() << '\n';
    return 0;
}
