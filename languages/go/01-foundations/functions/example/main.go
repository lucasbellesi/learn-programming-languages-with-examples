// Module focus: Breaking behavior into reusable functions with clear inputs and outputs.
// Why it matters: the example makes it possible to decompose a problem into focused functions
// with explicit contracts before the learner tackles the exercises.

package main

import "fmt"

// Separate helpers keep the main path focused on how to decompose a problem into focused
// functions with explicit contracts.
func add(a int, b int) int {
	return a + b
}

func swapInSlice(values []int, i int, j int) {
	values[i], values[j] = values[j], values[i]
}

func printSlice(values []int) {
	fmt.Println(values)
}

// Fixed inputs make the consequence of embedding all logic in main instead of reusable helpers
// visible and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	// The printed result shows whether the program can use parameters and return values without
	// hidden state changes.
	fmt.Println(add(4, 6))

	numbers := []int{10, 20, 30}
	printSlice(numbers)
	swapInSlice(numbers, 0, 1)
	printSlice(numbers)
}
