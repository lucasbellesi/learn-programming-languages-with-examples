// This example shows reading typed input carefully and turning raw text into values.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import "fmt"

// Run one deterministic scenario so the console output makes reading typed input carefully and turning raw text into values easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	var fullName string
	var age int
	var gpa float64

	// Print the observed state here so learners can connect the code path to a concrete result.
	fmt.Print("Enter your first name: ")
	fmt.Scanln(&fullName)

	fmt.Print("Enter your age: ")
	fmt.Scanln(&age)

	fmt.Print("Enter your GPA: ")
	fmt.Scanln(&gpa)

	fmt.Println("\n--- Student Summary ---")
	fmt.Printf("Name: %s\n", fullName)
	fmt.Printf("Age: %d\n", age)
	fmt.Printf("GPA: %.2f\n", gpa)
	fmt.Printf("Adult: %t\n", age >= 18)
}
