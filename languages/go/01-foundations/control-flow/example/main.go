// Module focus: Choosing between branches and repeating work with predictable control flow.
// Why it matters: the example makes it possible to select branches that cover normal and boundary
// conditions before the learner tackles the exercises.

package main

import "fmt"

// Fixed inputs make the consequence of not handling non-positive upper bounds before entering
// loops visible and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	var value int
	// The printed result shows whether the program can write terminating loops and reason about
	// their invariants.
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
