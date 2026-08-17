// Module focus: Storing related values in ordered collections and iterating safely.
// Why it matters: the example makes it possible to store and traverse ordered collections safely
// before the learner tackles the exercises.

package main

import "fmt"

// Fixed inputs make the consequence of trusting collection size input when count is zero or
// negative visible and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	fixedScores := [3]int{72, 88, 95}
	// The printed result shows whether the program can handle empty collections and index boundaries
	// explicitly.
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
