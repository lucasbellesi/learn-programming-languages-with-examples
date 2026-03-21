// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import "fmt"

func main() {
	// Program flow: collect input, apply core logic, then print a verifiable result.
	fixedScores := [3]int{72, 88, 95}
	// Intent: print intermediate or final output for quick behavior verification.
	fmt.Printf("Fixed array values: %d, %d, %d\n", fixedScores[0], fixedScores[1], fixedScores[2])

	var count int
	fmt.Print("How many temperatures do you want to enter? ")
	// Intent: gather typed input first so later operations are predictable.
	fmt.Scanln(&count)

	// Intent: guard invalid or edge-case paths before the main path continues.
	if count <= 0 {
		fmt.Println("Nothing to process.")
		return
	}

	temperatures := make([]float64, 0, count)
	// Intent: iterate through data in a clear and deterministic order.
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
