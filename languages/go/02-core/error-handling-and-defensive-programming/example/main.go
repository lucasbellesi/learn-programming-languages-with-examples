// Module focus: Guarding risky inputs so failures stay explicit and controlled.
// Why it matters: the example makes it possible to separate expected failures from programming
// defects before the learner tackles the exercises.

package main

import (
	"fmt"
)

// Separate helpers keep the main path focused on how to separate expected failures from
// programming defects.
func safeDivide(left float64, right float64) (float64, bool) {
	if right == 0.0 {
		return 0.0, false
	}
	return left / right, true
}

// Fixed inputs make the consequence of continuing execution after detecting invalid input visible
// and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	scenarios := [][2]float64{
		{42.0, 6.0},
		{10.0, 0.0},
	}

	for _, scenario := range scenarios {
		left := scenario[0]
		right := scenario[1]

		// The printed result shows whether the program can preserve valid state and useful diagnostics
		// when operations fail.
		fmt.Printf("Input: %v %v\n", left, right)

		quotient, ok := safeDivide(left, right)
		if !ok {
			fmt.Println("Cannot divide by zero.")
			continue
		}

		fmt.Printf("Result: %v\n", quotient)
	}
}
