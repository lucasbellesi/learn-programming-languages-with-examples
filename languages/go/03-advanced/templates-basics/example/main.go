// Module focus: Writing generic code that stays useful across multiple data types.
// Why it matters: practicing templates basics patterns makes exercises and checkpoints easier to reason about.

package main

import (
	"cmp"
	"fmt"
)

// Helper setup for templates basics; this keeps the walkthrough readable.
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

// Walk through one fixed scenario so templates basics behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key templates basics path.
	// Report values so learners can verify the templates basics outcome.
	fmt.Printf("MaxValue(4, 7) = %v\n", MaxValue(4, 7))
	fmt.Printf("MaxValue(2.5, 1.2) = %v\n", MaxValue(2.5, 1.2))

	pair := Pair[string]{First: "left", Second: "right"}
	pair.Print()
}
