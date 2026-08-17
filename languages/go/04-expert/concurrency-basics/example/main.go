// Module focus: Starting multiple units of work and combining their results safely.
// Why it matters: the example makes it possible to coordinate concurrent work without data races
// or lost results before the learner tackles the exercises.

package main

import (
	"fmt"
	"sync"
)

// Fixed inputs make the consequence of accessing shared state without a mutex visible and
// repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	const workerCount = 4
	const incrementsPerWorker = 10000

	counter := 0
	var counterMu sync.Mutex
	var wg sync.WaitGroup

	for workerIndex := 0; workerIndex < workerCount; workerIndex++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for step := 0; step < incrementsPerWorker; step++ {
				// Protect the shared counter so each increment is applied completely.
				counterMu.Lock()
				counter++
				counterMu.Unlock()
			}
		}()
	}

	wg.Wait()
	// The printed result shows whether the program can define completion, cancellation, and error
	// propagation behavior.
	fmt.Printf("Expected counter: %d\n", workerCount*incrementsPerWorker)
	fmt.Printf("Actual counter: %d\n", counter)

	fmt.Println("Producer-consumer demo:")
	// Channels pass ownership of each job value from producer to consumer.
	jobs := make(chan int)
	totals := make(chan int, 1)

	go func() {
		total := 0
		for value := range jobs {
			// The consumer owns aggregation, so no extra lock is needed for total.
			fmt.Printf("Consumed %d\n", value)
			total += value
		}
		totals <- total
	}()

	for _, value := range []int{10, 20, 30, 40} {
		fmt.Printf("Produced %d\n", value)
		jobs <- value
	}
	close(jobs)

	fmt.Printf("Consumed total: %d\n", <-totals)
}
