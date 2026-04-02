// Module focus: Modeling related data and behavior with structured types.
// Why it matters: practicing structs and classes patterns makes exercises and checkpoints easier to reason about.

package main

import "fmt"

// Helper setup for structs and classes; this keeps the walkthrough readable.
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

// Walk through one fixed scenario so structs and classes behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key structs and classes path.
	route := []Coordinate{{X: 2, Y: 3}, {X: -1, Y: 4}, {X: 5, Y: -2}}

	// Report values so learners can verify the structs and classes outcome.
	fmt.Println("Coordinates (struct example):")
	for _, point := range route {
		fmt.Printf("Point (%d, %d), Manhattan distance = %d\n", point.X, point.Y, point.ManhattanDistanceFromOrigin())
	}

	wallet := NewWallet("Maya", 120)
	wallet.Deposit(35)
	wallet.Withdraw(40)

	fmt.Println("\nWallet (class-style example):")
	fmt.Printf("Owner: %s\n", wallet.Owner())
	fmt.Printf("Balance: %.2f\n", wallet.Balance())
}
