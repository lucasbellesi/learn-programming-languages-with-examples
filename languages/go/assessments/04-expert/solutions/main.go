package main

import (
	"fmt"
	"sync"
)

type Summary struct {
	total   int
	minimum int
	maximum int
}

func main() {
	data := []int{12, 7, 25, 4, 31, 19, 2, 45, 18, 9, 27, 6}

	workerCount := 3
	chunkSize := (len(data) + workerCount - 1) / workerCount

	globalSummary := Summary{
		minimum: int(^uint(0) >> 1),
		maximum: -int(^uint(0)>>1) - 1,
	}

	var (
		wg   sync.WaitGroup
		lock sync.Mutex
	)

	for workerID := range workerCount {
		begin := workerID * chunkSize
		end := begin + chunkSize
		if end > len(data) {
			end = len(data)
		}

		wg.Add(1)
		go func(id int, start int, stop int) {
			defer wg.Done()

			if start >= stop {
				return
			}

			localTotal := 0
			localMin := data[start]
			localMax := data[start]

			for _, value := range data[start:stop] {
				localTotal += value
				if value < localMin {
					localMin = value
				}
				if value > localMax {
					localMax = value
				}
			}

			lock.Lock()
			fmt.Printf("Worker %d partial sum: %d\n", id, localTotal)
			globalSummary.total += localTotal
			if localMin < globalSummary.minimum {
				globalSummary.minimum = localMin
			}
			if localMax > globalSummary.maximum {
				globalSummary.maximum = localMax
			}
			lock.Unlock()
		}(workerID, begin, end)
	}

	wg.Wait()

	fmt.Println()
	fmt.Println("Final summary:")
	fmt.Printf("Total: %d\n", globalSummary.total)
	fmt.Printf("Minimum: %d\n", globalSummary.minimum)
	fmt.Printf("Maximum: %d\n", globalSummary.maximum)
}
