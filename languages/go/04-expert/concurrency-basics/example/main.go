// Example purpose: show goroutines, mutexes, and channels in one small runnable flow.

package main

import (
	"fmt"
	"sync"
)

func main() {
	// Program flow: first protect a shared counter, then coordinate producer-consumer work.
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

	// Intent: final output verifies the total collected by the consumer goroutine.
	fmt.Printf("Consumed total: %d\n", <-totals)
}
