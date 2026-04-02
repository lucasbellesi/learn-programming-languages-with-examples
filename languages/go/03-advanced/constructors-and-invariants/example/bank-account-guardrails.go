// This helper example focuses on showing how helper methods preserve invariants around deposits and withdrawals.

// This extra example extends constructors and invariants with a bank account.

package main

import (
	"fmt"
	"strings"
)

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
type BankAccount struct {
	owner   string
	balance float64
}

func NewBankAccount(owner string, initialBalance float64) BankAccount {
	cleanOwner := strings.TrimSpace(owner)
	if cleanOwner == "" {
		cleanOwner = "Unknown"
	}
	if initialBalance < 0.0 {
		initialBalance = 0.0
	}

	return BankAccount{
		owner:   cleanOwner,
		balance: initialBalance,
	}
}

func (account *BankAccount) Deposit(amount float64) bool {
	if amount <= 0.0 {
		return false
	}
	account.balance += amount
	return true
}

func (account *BankAccount) Withdraw(amount float64) bool {
	if amount <= 0.0 || amount > account.balance {
		return false
	}
	account.balance -= amount
	return true
}

func (account BankAccount) Summary() string {
	return fmt.Sprintf("%s: %.2f", account.owner, account.balance)
}

func main() {
	account := NewBankAccount("  Ana  ", -50.0)
	fmt.Printf("Initial: %s\n", account.Summary())
	fmt.Printf("Deposit 20 success: %t\n", account.Deposit(20.0))
	fmt.Printf("Withdraw 10 success: %t\n", account.Withdraw(10.0))
	fmt.Printf("Withdraw 99 success: %t\n", account.Withdraw(99.0))
	fmt.Printf("Final: %s\n", account.Summary())
}
