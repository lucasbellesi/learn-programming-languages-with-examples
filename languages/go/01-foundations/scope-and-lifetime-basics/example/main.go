// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import "fmt"

const PassingScore = 60

func classify(score int) string {
	switch {
	case score >= 90:
		return "A"
	case score >= 80:
		return "B"
	case score >= 70:
		return "C"
	case score >= PassingScore:
		return "D"
	default:
		return "F"
	}
}

func main() {
	// Program flow: collect input, apply core logic, then print a verifiable result.
	var score int
	// Intent: print intermediate or final output for quick behavior verification.
	fmt.Print("Enter score: ")
	// Intent: gather typed input first so later operations are predictable.
	fmt.Scanln(&score)

	grade := classify(score)
	fmt.Printf("Grade: %s\n", grade)
	fmt.Printf("Passed: %t\n", score >= PassingScore)
}
