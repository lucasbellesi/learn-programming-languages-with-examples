// Module focus: Tying resource cleanup to object lifetime so cleanup stays predictable.
// Why it matters: practicing memory management and raii patterns makes exercises and checkpoints easier to reason about.

package main

import "fmt"

// Helper setup for memory management and raii; this keeps the walkthrough readable.
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

// Walk through one fixed scenario so memory management and raii behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key memory management and raii path.
	active := 0
	// Report values so learners can verify the memory management and raii outcome.
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

	fmt.Printf("Active after scope: %d\n", active)
}
