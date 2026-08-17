// Module focus: Writing generic code that stays useful across multiple data types.
// Why it matters: the example makes it possible to express reusable type-safe behavior with
// language generics before the learner tackles the exercises.

package main

import (
	"cmp"
	"fmt"
)

// Separate helpers keep the main path focused on how to express reusable type-safe behavior with
// language generics.
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

// Fixed inputs make the consequence of assuming every type supports comparison or addition
// visible and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	// The printed result shows whether the program can apply constraints when an operation requires
	// specific capabilities.
	fmt.Printf("MaxValue(4, 7) = %v\n", MaxValue(4, 7))
	fmt.Printf("MaxValue(2.5, 1.2) = %v\n", MaxValue(2.5, 1.2))

	pair := Pair[string]{First: "left", Second: "right"}
	pair.Print()
}
