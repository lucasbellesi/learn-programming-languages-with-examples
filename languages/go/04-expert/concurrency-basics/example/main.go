// This example shows starting multiple units of work and combining their results safely.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import (
	"fmt"
	"sync"
)

// Run one deterministic scenario so the console output makes starting multiple units of work and combining their results safely easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
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
				counterMu.Lock()
				counter++
				counterMu.Unlock()
			}
		}()
	}

	wg.Wait()
	// Print the observed state here so learners can connect the code path to a concrete result.
	fmt.Printf("Expected counter: %d\n", workerCount*incrementsPerWorker)
	fmt.Printf("Actual counter: %d\n", counter)

	fmt.Println("Producer-consumer demo:")
	jobs := make(chan int)
	totals := make(chan int, 1)

	go func() {
		total := 0
		for value := range jobs {
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
