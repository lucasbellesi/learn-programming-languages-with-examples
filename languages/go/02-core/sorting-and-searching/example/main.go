// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import (
	"fmt"
	"sort"
)

func binarySearch(values []int, target int) int {
	left := 0
	right := len(values) - 1

	// Intent: shrink the search range based on sorted ordering guarantees.
	for left <= right {
		mid := left + (right-left)/2
		midValue := values[mid]

		// Intent: return as soon as we find an exact match.
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

func main() {
	// Program flow: sort values first, then run search on the sorted slice.
	values := []int{7, 2, 9, 4, 2, 8}
	sort.Ints(values)

	// Intent: print sorted values to verify binary-search preconditions.
	fmt.Printf("Sorted: %v\n", values)

	target := 4
	index := binarySearch(values, target)

	// Intent: handle not-found explicitly to keep behavior clear.
	if index >= 0 {
		fmt.Printf("Found %d at index %d\n", target, index)
	} else {
		fmt.Printf("%d not found\n", target)
	}
}
