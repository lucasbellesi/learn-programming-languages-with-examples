// Module focus: How names stay visible only inside the blocks that own them.
// Why it matters: practicing scope and lifetime basics patterns makes exercises and checkpoints easier to reason about.

package main

import "fmt"

// Helper setup for scope and lifetime basics; this keeps the walkthrough readable.
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

// Walk through one fixed scenario so scope and lifetime basics behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key scope and lifetime basics path.
	var score int
	// Report values so learners can verify the scope and lifetime basics outcome.
	fmt.Print("Enter score: ")
	fmt.Scanln(&score)

	grade := classify(score)
	fmt.Printf("Grade: %s\n", grade)
	fmt.Printf("Passed: %t\n", score >= PassingScore)
}
