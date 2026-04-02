// This example shows counting repeated values and summarizing them through keyed lookups.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import (
	"fmt"
	"sort"
)

// Run one deterministic scenario so the console output makes counting repeated values and summarizing them through keyed lookups easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	text := "banana bandana"
	frequencies := make(map[rune]int)

	for _, ch := range text {
		if ch == ' ' {
			continue
		}
		frequencies[ch]++
	}

	keys := make([]rune, 0, len(frequencies))
	for ch := range frequencies {
		keys = append(keys, ch)
	}
	sort.Slice(keys, func(i int, j int) bool { return keys[i] < keys[j] })

	// Print the observed state here so learners can connect the code path to a concrete result.
	fmt.Println("Character frequencies:")
	for _, key := range keys {
		fmt.Printf("%c -> %d\n", key, frequencies[key])
	}
}
