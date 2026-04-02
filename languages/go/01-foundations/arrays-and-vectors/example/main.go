// This example shows storing related values in ordered collections and iterating safely.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import "fmt"

// Run one deterministic scenario so the console output makes storing related values in ordered collections and iterating safely easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	fixedScores := [3]int{72, 88, 95}
	// Print the observed state here so learners can connect the code path to a concrete result.
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
