// This example shows tying resource cleanup to object lifetime so cleanup stays predictable.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import "fmt"

// Define the reusable pieces first so the main flow can focus on one observable scenario.
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

// Run one deterministic scenario so the console output makes tying resource cleanup to object lifetime so cleanup stays predictable easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	active := 0
	// Print the observed state here so learners can connect the code path to a concrete result.
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
