// Module focus: Reordering data and locating values with deliberate search logic.
// Why it matters: the example makes it possible to choose and apply sorting and searching
// operations correctly before the learner tackles the exercises.

package main

import (
	"fmt"
	"sort"
)

// Separate helpers keep the main path focused on how to choose and apply sorting and searching
// operations correctly.
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

// Fixed inputs make the consequence of applying binary search to unsorted values visible and
// repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	values := []int{7, 2, 9, 4, 2, 8}
	sort.Ints(values)

	// The printed result shows whether the program can explain ordering, duplicates, missing values,
	// and stability tradeoffs.
	fmt.Printf("Sorted: %v\n", values)

	target := 4
	index := binarySearch(values, target)

	if index >= 0 {
		fmt.Printf("Found %d at index %d\n", target, index)
	} else {
		fmt.Printf("%d not found\n", target)
	}
}
