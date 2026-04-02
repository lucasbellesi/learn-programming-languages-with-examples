// This example shows reordering data and locating values with deliberate search logic.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import (
	"fmt"
	"sort"
)

// Define the reusable pieces first so the main flow can focus on one observable scenario.
func binarySearch(values []int, target int) int {
	left := 0
	right := len(values) - 1

	for left <= right {
		mid := left + (right-left)/2
		midValue := values[mid]

		if midValue == target {
			return mid
		}

		if midValue < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return -1
}

// Run one deterministic scenario so the console output makes reordering data and locating values with deliberate search logic easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	values := []int{7, 2, 9, 4, 2, 8}
	sort.Ints(values)

	// Print the observed state here so learners can connect the code path to a concrete result.
	fmt.Printf("Sorted: %v\n", values)

	target := 4
	index := binarySearch(values, target)

	if index >= 0 {
		fmt.Printf("Found %d at index %d\n", target, index)
	} else {
		fmt.Printf("%d not found\n", target)
	}
}
