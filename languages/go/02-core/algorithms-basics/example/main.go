// Module focus: Walking data step by step to compute summaries and decisions.
// Why it matters: the example makes it possible to implement linear scans and accumulations with
// clear invariants before the learner tackles the exercises.

package main

import "fmt"

// Separate helpers keep the main path focused on how to implement linear scans and accumulations
// with clear invariants.
func linearSearch(values []int, target int) int {
	// A linear search is the direct choice when values are not sorted.
	for index, value := range values {
		if value == target {
			return index
		}
	}
	return -1
}

func countOccurrences(values []int, target int) int {
	count := 0
	// Counting is a separate pass here so learners can inspect one purpose at a time.
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

	// Seed from the first element so negative-only data is handled correctly.
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

// Fixed inputs make the consequence of ignoring empty-slice checks before min/max logic visible
// and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	values := []int{4, 7, 4, 1, 9, 4, 2}
	target := 4

	firstIndex := linearSearch(values, target)
	// The printed result shows whether the program can analyze behavior for empty, duplicate, and
	// missing values.
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
