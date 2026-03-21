// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import "fmt"

type Coordinate struct {
	X int
	Y int
}

func (c Coordinate) ManhattanDistanceFromOrigin() int {
	return abs(c.X) + abs(c.Y)
}

func abs(value int) int {
	if value < 0 {
		return -value
	}
	return value
}

type Wallet struct {
	owner   string
	balance float64
}

func NewWallet(owner string, initialBalance float64) *Wallet {
	if owner == "" {
		owner = "Unknown"
	}
	if initialBalance < 0 {
		initialBalance = 0
	}

	return &Wallet{owner: owner, balance: initialBalance}
}

func (w *Wallet) Deposit(amount float64) bool {
	if amount <= 0 {
		return false
	}
	w.balance += amount
	return true
}

func (w *Wallet) Withdraw(amount float64) bool {
	if amount <= 0 || amount > w.balance {
		return false
	}
	w.balance -= amount
	return true
}

func (w *Wallet) Owner() string {
	return w.owner
}

func (w *Wallet) Balance() float64 {
	return w.balance
}

func main() {
	// Program flow: inspect struct values, then apply class-like state transitions with methods.
	route := []Coordinate{{X: 2, Y: 3}, {X: -1, Y: 4}, {X: 5, Y: -2}}

	fmt.Println("Coordinates (struct example):")
	// Intent: deterministic iteration helps beginners verify output quickly.
	for _, point := range route {
		fmt.Printf("Point (%d, %d), Manhattan distance = %d\n", point.X, point.Y, point.ManhattanDistanceFromOrigin())
	}

	wallet := NewWallet("Maya", 120)
	wallet.Deposit(35)
	wallet.Withdraw(40)

	// Intent: report final state after guarded operations.
	fmt.Println("\nWallet (class-style example):")
	fmt.Printf("Owner: %s\n", wallet.Owner())
	fmt.Printf("Balance: %.2f\n", wallet.Balance())
}
