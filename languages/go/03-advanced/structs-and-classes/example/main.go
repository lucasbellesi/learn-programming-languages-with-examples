// Module focus: Modeling related data and behavior with structured types.
// Why it matters: the example makes it possible to model data and behavior with cohesive domain
// types before the learner tackles the exercises.

package main

import "fmt"

// Separate helpers keep the main path focused on how to model data and behavior with cohesive
// domain types.
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

// Fixed inputs make the consequence of mutating shared state without clear method boundaries
// visible and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	route := []Coordinate{{X: 2, Y: 3}, {X: -1, Y: 4}, {X: 5, Y: -2}}

	// The printed result shows whether the program can protect invariants through constructors and
	// methods.
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
