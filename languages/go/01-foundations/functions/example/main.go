// Module focus: Breaking behavior into reusable functions with clear inputs and outputs.
// Why it matters: practicing functions patterns makes exercises and checkpoints easier to reason about.

package main

import "fmt"

// Helper setup for functions; this keeps the walkthrough readable.
func add(a int, b int) int {
	return a + b
}

func swapInSlice(values []int, i int, j int) {
	values[i], values[j] = values[j], values[i]
}

func printSlice(values []int) {
	fmt.Println(values)
}

// Walk through one fixed scenario so functions behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key functions path.
	// Report values so learners can verify the functions outcome.
	fmt.Println(add(4, 6))

	numbers := []int{10, 20, 30}
	printSlice(numbers)
	swapInSlice(numbers, 0, 1)
	printSlice(numbers)
}
