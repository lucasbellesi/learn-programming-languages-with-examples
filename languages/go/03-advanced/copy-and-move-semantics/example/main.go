// Module focus: How copying, sharing, or transferring state changes later behavior.
// Why it matters: the example makes it possible to predict aliasing and independence after
// copying or sharing values before the learner tackles the exercises.

package main

import "fmt"

// Separate helpers keep the main path focused on how to predict aliasing and independence after
// copying or sharing values.
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

// Fixed inputs make the consequence of assuming `=` creates an independent deep copy for slices
// visible and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	first := NewBuffer(3)
	second := first.Clone()
	third := second.Transfer()

	// The printed result shows whether the program can choose an idiomatic ownership-transfer
	// strategy for the language.
	fmt.Printf("first size: %d\n", first.Size())
	fmt.Printf("second size (after transfer): %d\n", second.Size())
	fmt.Printf("third size: %d\n", third.Size())
}
