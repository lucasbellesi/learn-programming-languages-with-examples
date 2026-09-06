// Read a first name and numeric fields, then print a student summary.
// This first example assumes valid input; input-validation teaches error checks.

package main

import "fmt"

func main() {
	// Scanln reads whitespace-separated fields; use one word for the first name.
	var fullName string
	var age int
	var gpa float64

	// Enter valid numeric text here; Scanln returns an error when conversion fails.
	fmt.Print("Enter your first name: ")
	fmt.Scanln(&fullName)

	fmt.Print("Enter your age: ")
	fmt.Scanln(&age)

	fmt.Print("Enter your GPA: ")
	fmt.Scanln(&gpa)

	// Print GPA to two decimal places; the comparison produces a boolean.
	fmt.Println("\n--- Student Summary ---")
	fmt.Printf("Name: %s\n", fullName)
	fmt.Printf("Age: %d\n", age)
	fmt.Printf("GPA: %.2f\n", gpa)
	fmt.Printf("Adult: %t\n", age >= 18)
}
