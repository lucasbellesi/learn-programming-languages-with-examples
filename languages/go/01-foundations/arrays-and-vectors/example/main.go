// Module focus: Storing related values in ordered collections and iterating safely.
// Why it matters: practicing arrays and vectors patterns makes exercises and checkpoints easier to reason about.

package main

import "fmt"

// Walk through one fixed scenario so arrays and vectors behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key arrays and vectors path.
	fixedScores := [3]int{72, 88, 95}
	// Report values so learners can verify the arrays and vectors outcome.
	fmt.Printf("Fixed array values: %d, %d, %d\n", fixedScores[0], fixedScores[1], fixedScores[2])

	var count int
	fmt.Print("How many temperatures do you want to enter? ")
	fmt.Scanln(&count)

	if count <= 0 {
		fmt.Println("Nothing to process.")
		return
	}

	temperatures := make([]float64, 0, count)
	for i := 0; i < count; i++ {
		var value float64
		fmt.Printf("Temperature %d: ", i+1)
		fmt.Scanln(&value)
		temperatures = append(temperatures, value)
	}

	sum := 0.0
	for _, value := range temperatures {
		sum += value
	}

	average := sum / float64(len(temperatures))
	fmt.Printf("Average temperature: %.2f\n", average)
}
