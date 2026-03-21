// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import "fmt"

func main() {
	// Program flow: collect input, apply core logic, then print a verifiable result.
	var totalSeconds int
	// Intent: print intermediate or final output for quick behavior verification.
	fmt.Print("Enter total seconds: ")
	// Intent: gather typed input first so later operations are predictable.
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

	// Intent: guard invalid or edge-case paths before the main path continues.
	if b != 0 {
		fmt.Printf("Division: %.4f\n", a/b)
	} else {
		fmt.Println("Division is not possible because second number is zero.")
	}
}
