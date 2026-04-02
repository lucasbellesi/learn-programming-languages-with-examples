// Module focus: Walking data step by step to compute summaries and decisions.
// Why it matters: practicing algorithms basics patterns makes exercises and checkpoints easier to reason about.

package main

import "fmt"

// Helper setup for algorithms basics; this keeps the walkthrough readable.
func linearSearch(values []int, target int) int {
	for index, value := range values {
		if value == target {
			return index
		}
	}
	return -1
}

func countOccurrences(values []int, target int) int {
	count := 0
	for _, value := range values {
		if value == target {
			count++
		}
	}
	return count
}

func minMax(values []int) (int, int, bool) {
	if len(values) == 0 {
		return 0, 0, false
	}

	minValue := values[0]
	maxValue := values[0]
	for _, value := range values {
		if value < minValue {
			minValue = value
		}
		if value > maxValue {
			maxValue = value
		}
	}

	return minValue, maxValue, true
}

// Walk through one fixed scenario so algorithms basics behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key algorithms basics path.
	values := []int{4, 7, 4, 1, 9, 4, 2}
	target := 4

	firstIndex := linearSearch(values, target)
	// Report values so learners can verify the algorithms basics outcome.
	fmt.Printf("First index of %d: %d\n", target, firstIndex)
	fmt.Printf("Occurrences of %d: %d\n", target, countOccurrences(values, target))

	minValue, maxValue, ok := minMax(values)
	if !ok {
		fmt.Println("No values to process.")
		return
	}

	fmt.Printf("Minimum: %d\n", minValue)
	fmt.Printf("Maximum: %d\n", maxValue)
}
