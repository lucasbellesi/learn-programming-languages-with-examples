// Module focus: Reordering data and locating values with deliberate search logic.
// Why it matters: practicing sorting and searching patterns makes exercises and checkpoints easier to reason about.

package main

import (
	"fmt"
	"sort"
)

// Helper setup for sorting and searching; this keeps the walkthrough readable.
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

// Walk through one fixed scenario so sorting and searching behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key sorting and searching path.
	values := []int{7, 2, 9, 4, 2, 8}
	sort.Ints(values)

	// Report values so learners can verify the sorting and searching outcome.
	fmt.Printf("Sorted: %v\n", values)

	target := 4
	index := binarySearch(values, target)

	if index >= 0 {
		fmt.Printf("Found %d at index %d\n", target, index)
	} else {
		fmt.Printf("%d not found\n", target)
	}
}
