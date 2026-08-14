package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
)

type partialResult struct {
	worker int
	sum    int
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Values: ")
	line, _ := reader.ReadString('\n')
	values, ok := parseValues(line)
	if !ok || len(values) == 0 {
		fmt.Println("No valid values provided.")
		return
	}

	fmt.Print("Worker count: ")
	line, _ = reader.ReadString('\n')
	workers, err := strconv.Atoi(strings.TrimSpace(line))
	if err != nil {
		fmt.Println("Invalid worker count.")
		return
	}
	if workers <= 0 {
		fmt.Println("Worker count must be positive.")
		return
	}

	workerCount := workers
	if workerCount > len(values) {
		workerCount = len(values)
	}
	chunkSize := (len(values) + workerCount - 1) / workerCount

	results := make(chan partialResult, workerCount)
	var wg sync.WaitGroup

	for workerIndex := 0; workerIndex < workerCount; workerIndex++ {
		start := workerIndex * chunkSize
		end := start + chunkSize
		if end > len(values) {
			end = len(values)
		}

		wg.Add(1)
		go func(index, from, to int) {
			defer wg.Done()
			partial := 0
			for _, value := range values[from:to] {
				partial += value
			}
			results <- partialResult{worker: index + 1, sum: partial}
		}(workerIndex, start, end)
	}

	wg.Wait()
	close(results)

	total := 0
	for result := range results {
		fmt.Printf("Worker %d partial: %d\n", result.worker, result.sum)
		total += result.sum
	}
	fmt.Printf("Total: %d\n", total)
}

func parseValues(raw string) ([]int, bool) {
	fields := strings.Fields(raw)
	values := make([]int, 0, len(fields))
	for _, field := range fields {
		value, err := strconv.Atoi(field)
		if err != nil {
			return nil, false
		}
		values = append(values, value)
	}
	return values, true
}
