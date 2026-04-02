// This example shows how names stay visible only inside the blocks that own them.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import "fmt"

// Define the reusable pieces first so the main flow can focus on one observable scenario.
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

// Run one deterministic scenario so the console output makes how names stay visible only inside the blocks that own them easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	var score int
	// Print the observed state here so learners can connect the code path to a concrete result.
	fmt.Print("Enter score: ")
	fmt.Scanln(&score)

	grade := classify(score)
	fmt.Printf("Grade: %s\n", grade)
	fmt.Printf("Passed: %t\n", score >= PassingScore)
}
