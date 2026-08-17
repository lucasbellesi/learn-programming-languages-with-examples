// Module focus: How names stay visible only inside the blocks that own them.
// Why it matters: the example makes it possible to predict name visibility across nested scopes
// before the learner tackles the exercises.

package main

import "fmt"

// Separate helpers keep the main path focused on how to predict name visibility across nested
// scopes.
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

// Fixed inputs make the consequence of using values before they are assigned in all branches
// visible and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	var score int
	// The printed result shows whether the program can explain when values and resources cease to be
	// usable.
	fmt.Print("Enter score: ")
	fmt.Scanln(&score)

	grade := classify(score)
	fmt.Printf("Grade: %s\n", grade)
	fmt.Printf("Passed: %t\n", score >= PassingScore)
}
