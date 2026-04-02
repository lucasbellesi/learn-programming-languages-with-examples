// This example shows breaking behavior into reusable functions with clear inputs and outputs.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import "fmt"

// Define the reusable pieces first so the main flow can focus on one observable scenario.
func add(a int, b int) int {
	return a + b
}

func swapInSlice(values []int, i int, j int) {
	values[i], values[j] = values[j], values[i]
}

func printSlice(values []int) {
	fmt.Println(values)
}

// Run one deterministic scenario so the console output makes breaking behavior into reusable functions with clear inputs and outputs easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	// Print the observed state here so learners can connect the code path to a concrete result.
	fmt.Println(add(4, 6))

	numbers := []int{10, 20, 30}
	printSlice(numbers)
	swapInSlice(numbers, 0, 1)
	printSlice(numbers)
}
