package main

import "fmt"

func main() {
	var score int
	fmt.Print("Enter score (0-100): ")
	fmt.Scanln(&score)

	if score < 0 || score > 100 {
		fmt.Println("Score must be between 0 and 100.")
		return
	}

	grade := "F"
	if score >= 90 {
		grade = "A"
	} else if score >= 80 {
		grade = "B"
	} else if score >= 70 {
		grade = "C"
	} else if score >= 60 {
		grade = "D"
	}

	fmt.Printf("Grade: %s\n", grade)
}
