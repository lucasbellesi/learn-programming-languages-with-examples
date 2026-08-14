package main

import "fmt"

type ownedBuffer struct {
	values []int
	closed bool
}

func newOwnedBuffer(size int) *ownedBuffer {
	return &ownedBuffer{values: make([]int, size)}
}

func (b *ownedBuffer) setAt(index, value int) {
	b.ensureOpen()
	b.values[index] = value
}

func (b *ownedBuffer) getAt(index int) int {
	b.ensureOpen()
	return b.values[index]
}

func (b *ownedBuffer) sum() int {
	b.ensureOpen()
	total := 0
	for _, value := range b.values {
		total += value
	}
	return total
}

func (b *ownedBuffer) Close() {
	if b.closed {
		return
	}
	b.closed = true
	b.values = nil
}

func (b *ownedBuffer) ensureOpen() {
	if b.closed {
		panic("buffer already closed")
	}
}

func main() {
	var count int
	fmt.Print("Count: ")
	if _, err := fmt.Scan(&count); err != nil {
		fmt.Println("Invalid count.")
		return
	}
	if count <= 0 {
		fmt.Println("Count must be positive.")
		return
	}

	buffer := newOwnedBuffer(count)
	defer buffer.Close()

	for index := 0; index < count; index++ {
		var value int
		fmt.Printf("Value %d: ", index+1)
		if _, err := fmt.Scan(&value); err != nil {
			fmt.Println("Invalid integer input.")
			return
		}
		buffer.setAt(index, value)
	}

	fmt.Printf("Sum: %d\n", buffer.sum())
	fmt.Print("Reversed:")
	for index := count - 1; index >= 0; index-- {
		fmt.Printf(" %d", buffer.getAt(index))
	}
	fmt.Println()
}
