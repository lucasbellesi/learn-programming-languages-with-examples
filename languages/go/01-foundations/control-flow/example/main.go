// Module focus: Choosing between branches and repeating work with predictable control flow.
// Why it matters: practicing control flow patterns makes exercises and checkpoints easier to reason about.

package main

import "fmt"

// Walk through one fixed scenario so control flow behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key control flow path.
	var value int
	// Report values so learners can verify the control flow outcome.
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
