package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

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
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Print("Buffer size: ")
	if !scanner.Scan() {
		fmt.Println("Invalid size.")
		return
	}

	size, err := strconv.Atoi(strings.TrimSpace(scanner.Text()))
	if err != nil || size < 0 {
		fmt.Println("Invalid size.")
		return
	}

	fmt.Print("Buffer values: ")
	if !scanner.Scan() {
		fmt.Println("The amount of values must match the buffer size.")
		return
	}

	parts := strings.Fields(scanner.Text())
	if len(parts) != size {
		fmt.Println("The amount of values must match the buffer size.")
		return
	}

	values := make([]int, 0, size)
	for _, part := range parts {
		value, parseErr := strconv.Atoi(part)
		if parseErr != nil {
			fmt.Println("Invalid value detected.")
			return
		}
		values = append(values, value)
	}

	a := NewIntBuffer(len(values))
	copy(a.values, values)
	b := a.Clone()
	c := b.Transfer()

	fmt.Printf("a size: %d\n", a.Size())
	fmt.Printf("b size: %d\n", b.Size())
	fmt.Printf("c size: %d\n", c.Size())
}
