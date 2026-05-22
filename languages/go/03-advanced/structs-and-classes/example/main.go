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
	// Value-style methods can compute from fields without changing the struct.
	x, y := c.X, c.Y
	if x < 0 {
		x = -x
	}
	if y < 0 {
		y = -y
	}
	return x + y
}

type Wallet struct {
	Owner   string
	Balance float64
}

func (w *Wallet) Apply(amount float64) bool {
	// Pointer-style methods update state while protecting the invariant.
	if w.Balance+amount < 0 {
		return false
	}
	w.Balance += amount
	return true
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

	wallet := Wallet{Owner: "Maya", Balance: 120}
	wallet.Apply(35)
	wallet.Apply(-40)

	fmt.Println("\nWallet (class-style example):")
	fmt.Printf("Owner: %s\n", wallet.Owner)
	fmt.Printf("Balance: %.2f\n", wallet.Balance)
}
