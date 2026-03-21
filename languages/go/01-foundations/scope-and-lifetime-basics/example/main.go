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
	var score int
	fmt.Print("Enter score: ")
	fmt.Scanln(&score)

	grade := classify(score)
	fmt.Printf("Grade: %s\n", grade)
	fmt.Printf("Passed: %t\n", score >= PassingScore)
}
