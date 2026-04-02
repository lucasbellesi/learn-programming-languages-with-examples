// Module focus: Reading typed input carefully and turning raw text into values.
// Why it matters: practicing types and io patterns makes exercises and checkpoints easier to reason about.

package main

import "fmt"

// Walk through one fixed scenario so types and io behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key types and io path.
	var fullName string
	var age int
	var gpa float64

	// Report values so learners can verify the types and io outcome.
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
