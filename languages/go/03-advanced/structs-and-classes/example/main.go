// This example shows modeling related data and behavior with structured types.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import "fmt"

// Define the reusable pieces first so the main flow can focus on one observable scenario.
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

// Run one deterministic scenario so the console output makes modeling related data and behavior with structured types easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	route := []Coordinate{{X: 2, Y: 3}, {X: -1, Y: 4}, {X: 5, Y: -2}}

	// Print the observed state here so learners can connect the code path to a concrete result.
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
