// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import "fmt"

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
	// Intent: deep copy isolates future changes between instances.
	copyValues := append([]int(nil), b.values...)
	fmt.Println("Cloned")
	return &Buffer{values: copyValues}
}

func (b *Buffer) Transfer() *Buffer {
	// Intent: transfer operation hands over current data and resets source.
	movedValues := b.values
	b.values = make([]int, 0)
	return newTransferredBuffer(movedValues)
}

func (b *Buffer) Size() int {
	return len(b.values)
}

func main() {
	// Program flow: create, clone, transfer, then inspect resulting states.
	first := NewBuffer(3)
	second := first.Clone()
	third := second.Transfer()

	fmt.Printf("first size: %d\n", first.Size())
	fmt.Printf("second size (after transfer): %d\n", second.Size())
	fmt.Printf("third size: %d\n", third.Size())
}
