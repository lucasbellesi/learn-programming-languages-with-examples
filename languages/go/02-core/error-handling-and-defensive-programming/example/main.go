// This example shows guarding risky inputs so failures stay explicit and controlled.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import (
	"fmt"
)

// Define the reusable pieces first so the main flow can focus on one observable scenario.
func safeDivide(left float64, right float64) (float64, bool) {
	if right == 0.0 {
		return 0.0, false
	}
	return left / right, true
}

// Run one deterministic scenario so the console output makes guarding risky inputs so failures stay explicit and controlled easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	scenarios := [][2]float64{
		{42.0, 6.0},
		{10.0, 0.0},
	}

	for _, scenario := range scenarios {
		left := scenario[0]
		right := scenario[1]

		// Print the observed state here so learners can connect the code path to a concrete result.
		fmt.Printf("Input: %v %v\n", left, right)

		quotient, ok := safeDivide(left, right)
		if !ok {
			fmt.Println("Cannot divide by zero.")
			continue
		}

		fmt.Printf("Result: %v\n", quotient)
	}
}
