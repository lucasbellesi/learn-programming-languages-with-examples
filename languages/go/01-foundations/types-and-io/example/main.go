// This example demonstrates types and io concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import "fmt"

func main() {
	// Program flow: collect input, apply core logic, then print a verifiable result.
	var fullName string
	var age int
	var gpa float64

	// Intent: print intermediate or final output for quick behavior verification.
	fmt.Print("Enter your first name: ")
	// Intent: gather typed input first so later operations are predictable.
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
