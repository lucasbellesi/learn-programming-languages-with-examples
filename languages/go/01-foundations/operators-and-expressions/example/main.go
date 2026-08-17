// Module focus: Combining values through expressions and readable calculations.
// Why it matters: the example makes it possible to build expressions with correct precedence and
// explicit intent before the learner tackles the exercises.

package main

import "fmt"

// Fixed inputs make the consequence of forgetting to reject negative totals for time conversion
// or subtotal visible and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	var totalSeconds int
	// The printed result shows whether the program can distinguish arithmetic, comparison, and
	// logical operations.
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
