// This example shows how copying, sharing, or transferring state changes later behavior.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import "fmt"

// Define the reusable pieces first so the main flow can focus on one observable scenario.
type Buffer struct {
	values []int
}

func NewBuffer(size int) *Buffer {
	if size < 0 {
		size = 0
	}
	fmt.Printf("Constructed (size=%d)\n", size)
	return &Buffer{values: make([]int, size)}
}

func newTransferredBuffer(values []int) *Buffer {
	fmt.Printf("Transferred (size=%d)\n", len(values))
	return &Buffer{values: values}
}

func (b *Buffer) Clone() *Buffer {
	copyValues := append([]int(nil), b.values...)
	fmt.Println("Cloned")
	return &Buffer{values: copyValues}
}

func (b *Buffer) Transfer() *Buffer {
	movedValues := b.values
	b.values = make([]int, 0)
	return newTransferredBuffer(movedValues)
}

func (b *Buffer) Size() int {
	return len(b.values)
}

// Run one deterministic scenario so the console output makes how copying, sharing, or transferring state changes later behavior easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	first := NewBuffer(3)
	second := first.Clone()
	third := second.Transfer()

	// Print the observed state here so learners can connect the code path to a concrete result.
	fmt.Printf("first size: %d\n", first.Size())
	fmt.Printf("second size (after transfer): %d\n", second.Size())
	fmt.Printf("third size: %d\n", third.Size())
}
