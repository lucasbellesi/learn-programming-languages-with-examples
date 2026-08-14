package main

import "fmt"

type BankAccount struct {
	balance float64
}

func NewBankAccount(initialBalance float64) *BankAccount {
	if initialBalance < 0 {
		initialBalance = 0
	}
	return &BankAccount{balance: initialBalance}
}

func (a *BankAccount) Deposit(amount float64) bool {
	if amount <= 0 {
		return false
	}
	a.balance += amount
	return true
}

func (a *BankAccount) Withdraw(amount float64) bool {
	if amount <= 0 || amount > a.balance {
		return false
	}
	a.balance -= amount
	return true
}

func (a *BankAccount) Balance() float64 {
	return a.balance
}

func main() {
	var initialBalance float64
	fmt.Print("Initial balance: ")
	if _, err := fmt.Scan(&initialBalance); err != nil {
		fmt.Println("Invalid initial balance.")
		return
	}

	account := NewBankAccount(initialBalance)

	var depositAmount float64
	fmt.Print("Deposit amount: ")
	if _, err := fmt.Scan(&depositAmount); err == nil {
		account.Deposit(depositAmount)
	}

	var withdrawAmount float64
	fmt.Print("Withdraw amount: ")
	if _, err := fmt.Scan(&withdrawAmount); err == nil {
		if !account.Withdraw(withdrawAmount) {
			fmt.Println("Withdrawal rejected.")
		}
	}

	fmt.Printf("Final balance: %v\n", account.Balance())
}
