// This example shows combining values through expressions and readable calculations.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import "fmt"

// Run one deterministic scenario so the console output makes combining values through expressions and readable calculations easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	var totalSeconds int
	// Print the observed state here so learners can connect the code path to a concrete result.
	fmt.Print("Enter total seconds: ")
	fmt.Scanln(&totalSeconds)

	hours := totalSeconds / 3600
	minutes := (totalSeconds % 3600) / 60
	seconds := totalSeconds % 60

	fmt.Printf("Time: %d:%02d:%02d\n", hours, minutes, seconds)

	var a, b float64
	fmt.Print("Enter first number: ")
	fmt.Scanln(&a)
	fmt.Print("Enter second number: ")
	fmt.Scanln(&b)

	fmt.Printf("Sum: %.4f\n", a+b)
	fmt.Printf("Difference: %.4f\n", a-b)
	fmt.Printf("Product: %.4f\n", a*b)

	if b != 0 {
		fmt.Printf("Division: %.4f\n", a/b)
	} else {
		fmt.Println("Division is not possible because second number is zero.")
	}
}
