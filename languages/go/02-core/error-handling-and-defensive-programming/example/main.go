// Module focus: Guarding risky inputs so failures stay explicit and controlled.
// Why it matters: practicing error handling and defensive programming patterns makes exercises and checkpoints easier to reason about.

package main

import (
	"fmt"
)

// Helper setup for error handling and defensive programming; this keeps the walkthrough readable.
func safeDivide(left float64, right float64) (float64, bool) {
	if right == 0.0 {
		return 0.0, false
	}
	return left / right, true
}

// Walk through one fixed scenario so error handling and defensive programming behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key error handling and defensive programming path.
	scenarios := [][2]float64{
		{42.0, 6.0},
		{10.0, 0.0},
	}

	for _, scenario := range scenarios {
		left := scenario[0]
		right := scenario[1]

		// Report values so learners can verify the error handling and defensive programming outcome.
		fmt.Printf("Input: %v %v\n", left, right)

		quotient, ok := safeDivide(left, right)
		if !ok {
			fmt.Println("Cannot divide by zero.")
			continue
		}

		fmt.Printf("Result: %v\n", quotient)
	}
}
