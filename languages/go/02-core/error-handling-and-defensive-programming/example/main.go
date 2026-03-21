// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import (
	"fmt"
)

func safeDivide(left float64, right float64) (float64, bool) {
	// Intent: block invalid operations before computing the result.
	if right == 0.0 {
		return 0.0, false
	}
	return left / right, true
}

func main() {
	// Program flow: run fixed scenarios to show both valid and invalid paths.
	scenarios := [][2]float64{
		{42.0, 6.0},
		{10.0, 0.0},
	}

	for _, scenario := range scenarios {
		left := scenario[0]
		right := scenario[1]

		// Intent: print scenario input so behavior is easy to verify.
		fmt.Printf("Input: %v %v\n", left, right)

		quotient, ok := safeDivide(left, right)
		if !ok {
			fmt.Println("Cannot divide by zero.")
			continue
		}

		// Intent: print deterministic final output for quick verification.
		fmt.Printf("Result: %v\n", quotient)
	}
}
