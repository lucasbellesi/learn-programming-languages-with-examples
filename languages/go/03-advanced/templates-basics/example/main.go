// This example shows writing generic code that stays useful across multiple data types.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import (
	"cmp"
	"fmt"
)

// Define the reusable pieces first so the main flow can focus on one observable scenario.
func MaxValue[T cmp.Ordered](left T, right T) T {
	if left > right {
		return left
	}
	return right
}

type Pair[T any] struct {
	First  T
	Second T
}

func (p Pair[T]) Print() {
	fmt.Printf("(%v, %v)\n", p.First, p.Second)
}

// Run one deterministic scenario so the console output makes writing generic code that stays useful across multiple data types easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	// Print the observed state here so learners can connect the code path to a concrete result.
	fmt.Printf("MaxValue(4, 7) = %v\n", MaxValue(4, 7))
	fmt.Printf("MaxValue(2.5, 1.2) = %v\n", MaxValue(2.5, 1.2))

	pair := Pair[string]{First: "left", Second: "right"}
	pair.Print()
}
