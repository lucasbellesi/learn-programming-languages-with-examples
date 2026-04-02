// Module focus: How copying, sharing, or transferring state changes later behavior.
// Why it matters: practicing copy and move semantics patterns makes exercises and checkpoints easier to reason about.

package main

import "fmt"

// Helper setup for copy and move semantics; this keeps the walkthrough readable.
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

// Walk through one fixed scenario so copy and move semantics behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key copy and move semantics path.
	first := NewBuffer(3)
	second := first.Clone()
	third := second.Transfer()

	// Report values so learners can verify the copy and move semantics outcome.
	fmt.Printf("first size: %d\n", first.Size())
	fmt.Printf("second size (after transfer): %d\n", second.Size())
	fmt.Printf("third size: %d\n", third.Size())
}
