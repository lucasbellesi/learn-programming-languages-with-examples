package main

import "fmt"

type IntBuffer struct {
	values []int
}

func NewIntBuffer(size int) *IntBuffer {
	if size < 0 {
		size = 0
	}
	fmt.Printf("Constructed IntBuffer (size=%d)\n", size)
	return &IntBuffer{values: make([]int, size)}
}

func (b *IntBuffer) Clone() *IntBuffer {
	copyValues := append([]int(nil), b.values...)
	fmt.Println("Cloned IntBuffer")
	return &IntBuffer{values: copyValues}
}

func (b *IntBuffer) Transfer() *IntBuffer {
	movedValues := b.values
	b.values = make([]int, 0)
	fmt.Printf("Transferred IntBuffer (size=%d)\n", len(movedValues))
	return &IntBuffer{values: movedValues}
}

func (b *IntBuffer) Size() int {
	return len(b.values)
}

func main() {
	a := NewIntBuffer(4)
	b := a.Clone()
	c := b.Transfer()

	fmt.Printf("a size: %d\n", a.Size())
	fmt.Printf("b size: %d\n", b.Size())
	fmt.Printf("c size: %d\n", c.Size())
}
