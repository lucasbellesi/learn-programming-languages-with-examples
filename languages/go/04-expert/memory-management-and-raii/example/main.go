// Module focus: Tying resource cleanup to object lifetime so cleanup stays predictable.
// Why it matters: the example makes it possible to explain the language's resource and memory
// lifetime model before the learner tackles the exercises.

package main

import "fmt"

// Separate helpers keep the main path focused on how to explain the language's resource and
// memory lifetime model.
type trackedBuffer struct {
	name   string
	values []int
	closed bool
	active *int
}

func newTrackedBuffer(name string, size int, active *int) *trackedBuffer {
	// Acquisition updates shared state immediately so cleanup can be verified later.
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
	// Close is idempotent so deferred cleanup is safe even if called manually first.
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

// Fixed inputs make the consequence of assuming the garbage collector closes resources on time
// visible and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	active := 0
	// The printed result shows whether the program can guarantee deterministic cleanup for
	// non-memory resources.
	fmt.Printf("Active before scope: %d\n", active)

	func() {
		scores := newTrackedBuffer("scores", 5, &active)
		// defer mirrors RAII-style cleanup at the end of this local scope.
		defer scores.Close()
		scores.fillSequence(10, 5)
		fmt.Printf("Scores: %s\n", scores.describe())
		fmt.Printf("Sum: %d\n", scores.sum())

		scratch := newTrackedBuffer("scratch", 3, &active)
		// Multiple deferred cleanups run even when the scope has several resources.
		defer scratch.Close()
		scratch.fillSequence(1, 1)
		fmt.Printf("Scratch: %s\n", scratch.describe())
		fmt.Printf("Active inside scope: %d\n", active)
	}()

	fmt.Printf("Active after scope: %d\n", active)
}
