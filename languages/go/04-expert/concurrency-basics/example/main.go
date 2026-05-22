// Module focus: Starting multiple units of work and combining their results safely.
// Why it matters: practicing concurrency basics patterns makes exercises and checkpoints easier to reason about.

package main

import (
	"fmt"
	"sync"
)

// Walk through one fixed scenario so concurrency basics behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key concurrency basics path.
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
	// Report values so learners can verify the concurrency basics outcome.
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
