// Module focus: Combining values through expressions and readable calculations.
// Why it matters: practicing operators and expressions patterns makes exercises and checkpoints easier to reason about.

package main

import "fmt"

// Walk through one fixed scenario so operators and expressions behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key operators and expressions path.
	var totalSeconds int
	// Report values so learners can verify the operators and expressions outcome.
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
