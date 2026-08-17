// Module focus: Reading typed input carefully and turning raw text into values.
// Why it matters: the example makes it possible to choose suitable primitive values and variables
// for a small problem before the learner tackles the exercises.

package main

import "fmt"

// Fixed inputs make the consequence of assuming input parsing always succeeds without validation
// visible and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	var fullName string
	var age int
	var gpa float64

	// The printed result shows whether the program can read, validate, transform, and present
	// console data.
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
