// This helper example focuses on contrasting two sorting behaviors without extra setup noise.

// This extra example extends sorting-and-searching with tie-order comparisons.

package main

import (
	"fmt"
	"sort"
)

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
type record struct {
	score int
	name  string
}

func printRecords(records []record, title string) {
	fmt.Println(title)
	for _, current := range records {
		fmt.Printf("- score=%d, name=%s\n", current.score, current.name)
	}
	fmt.Println()
}

func main() {
	records := []record{
		{score: 90, name: "Ana"},
		{score: 75, name: "Bob"},
		{score: 90, name: "Carla"},
		{score: 75, name: "Diego"},
		{score: 90, name: "Emma"},
	}

	printRecords(records, "Original order:")

	unstable := append([]record(nil), records...)
	sort.Slice(unstable, func(left int, right int) bool {
		return unstable[left].score < unstable[right].score
	})
	printRecords(unstable, "After sort.Slice (not guaranteed stable):")

	stable := append([]record(nil), records...)
	sort.SliceStable(stable, func(left int, right int) bool {
		return stable[left].score < stable[right].score
	})
	printRecords(stable, "After sort.SliceStable:")

	fmt.Println("Notice how equal scores keep their relative order with SliceStable.")
}
