// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import (
	"fmt"
	"sort"
)

func main() {
	// Program flow: iterate text, count characters, then print a frequency table.
	text := "banana bandana"
	frequencies := make(map[rune]int)

	// Intent: process characters in deterministic input order before aggregation.
	for _, ch := range text {
		// Intent: skip separators so counts focus on meaningful symbols.
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

	// Intent: print aggregated frequencies in sorted key order.
	fmt.Println("Character frequencies:")
	for _, key := range keys {
		fmt.Printf("%c -> %d\n", key, frequencies[key])
	}
}
