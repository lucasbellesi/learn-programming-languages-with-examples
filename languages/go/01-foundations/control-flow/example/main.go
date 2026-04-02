// This example shows choosing between branches and repeating work with predictable control flow.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import "fmt"

// Run one deterministic scenario so the console output makes choosing between branches and repeating work with predictable control flow easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	var value int
	// Print the observed state here so learners can connect the code path to a concrete result.
	fmt.Print("Enter an integer: ")
	fmt.Scanln(&value)

	if value > 0 {
		fmt.Println("positive")
	} else if value < 0 {
		fmt.Println("negative")
	} else {
		fmt.Println("zero")
	}

	var n int
	fmt.Print("Enter N: ")
	fmt.Scanln(&n)

	if n < 0 {
		fmt.Println("N must be non-negative.")
		return
	}

	factorial := 1
	for i := 1; i <= n; i++ {
		factorial *= i
	}

	fmt.Printf("factorial(%d) = %d\n", n, factorial)
	fmt.Println("Numbers 1..N:")
	for i := 1; i <= n; i++ {
		fmt.Println(i)
	}
}
