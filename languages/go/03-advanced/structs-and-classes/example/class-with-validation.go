// This helper example focuses on keeping validation close to the type that owns the data.

// This extra example extends structs-and-classes with validated object state.

package main

import (
	"errors"
	"fmt"
)

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
type bankAccount struct {
	owner   string
	balance float64
}

func newBankAccount(owner string, initialBalance float64) (*bankAccount, error) {
	if owner == "" {
		return nil, errors.New("owner name cannot be empty")
	}
	if initialBalance < 0.0 {
		return nil, errors.New("initial balance cannot be negative")
	}

	return &bankAccount{
		owner:   owner,
		balance: initialBalance,
	}, nil
}

func (account *bankAccount) deposit(amount float64) bool {
	if amount <= 0.0 {
		return false
	}
	account.balance += amount
	return true
}

func (account *bankAccount) withdraw(amount float64) bool {
	if amount <= 0.0 || amount > account.balance {
		return false
	}
	account.balance -= amount
	return true
}

func main() {
	account, err := newBankAccount("Ana Smith", 100.0)
	if err != nil {
		fmt.Printf("Error: %s\n", err)
		return
	}

	fmt.Printf("Account owner: %s\n", account.owner)
	fmt.Printf("Initial balance: %v\n", account.balance)

	if account.deposit(50.0) {
		fmt.Println("Deposit successful.")
	}
	if account.withdraw(30.0) {
		fmt.Println("Withdraw successful.")
	}
	if !account.withdraw(500.0) {
		fmt.Println("Withdraw rejected (insufficient funds).")
	}

	fmt.Printf("Final balance: %v\n", account.balance)
}
