// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import (
	"cmp"
	"fmt"
)

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
	// Intent: print final state from a generic container in one predictable format.
	fmt.Printf("(%v, %v)\n", p.First, p.Second)
}

func main() {
	// Program flow: call one generic function, then inspect one generic struct instance.
	fmt.Printf("MaxValue(4, 7) = %v\n", MaxValue(4, 7))
	fmt.Printf("MaxValue(2.5, 1.2) = %v\n", MaxValue(2.5, 1.2))

	pair := Pair[string]{First: "left", Second: "right"}
	pair.Print()
}
