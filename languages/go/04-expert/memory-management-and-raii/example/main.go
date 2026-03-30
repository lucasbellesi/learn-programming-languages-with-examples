// Example purpose: show deterministic cleanup with Close and defer in Go.

package main

import "fmt"

type trackedBuffer struct {
	name   string
	values []int
	closed bool
	active *int
}

func newTrackedBuffer(name string, size int, active *int) *trackedBuffer {
	*active += 1
	fmt.Printf("[acquire] %s size=%d active=%d\n", name, size, *active)
	return &trackedBuffer{name: name, values: make([]int, size), active: active}
}

func (b *trackedBuffer) fillSequence(start, step int) {
	b.ensureOpen()
	for index := range b.values {
		b.values[index] = start + (index * step)
	}
}

func (b *trackedBuffer) sum() int {
	b.ensureOpen()
	total := 0
	for _, value := range b.values {
		total += value
	}
	return total
}

func (b *trackedBuffer) describe() string {
	b.ensureOpen()
	return fmt.Sprint(b.values)
}

func (b *trackedBuffer) Close() {
	if b.closed {
		return
	}
	b.closed = true
	b.values = nil
	*b.active -= 1
	fmt.Printf("[close] %s active=%d\n", b.name, *b.active)
}

func (b *trackedBuffer) ensureOpen() {
	if b.closed {
		panic("buffer already closed")
	}
}

func main() {
	// Program flow: create scoped buffers, do work, and rely on deferred cleanup.
	active := 0
	fmt.Printf("Active before scope: %d\n", active)

	func() {
		scores := newTrackedBuffer("scores", 5, &active)
		defer scores.Close()
		scores.fillSequence(10, 5)
		fmt.Printf("Scores: %s\n", scores.describe())
		fmt.Printf("Sum: %d\n", scores.sum())

		scratch := newTrackedBuffer("scratch", 3, &active)
		defer scratch.Close()
		scratch.fillSequence(1, 1)
		fmt.Printf("Scratch: %s\n", scratch.describe())
		fmt.Printf("Active inside scope: %d\n", active)
	}()

	// Intent: final state confirms that deferred cleanup ran at scope exit.
	fmt.Printf("Active after scope: %d\n", active)
}
