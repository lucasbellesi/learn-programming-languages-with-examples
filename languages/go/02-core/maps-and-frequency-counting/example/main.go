// Module focus: Counting repeated values and summarizing them through keyed lookups.
// Why it matters: practicing maps and frequency counting patterns makes exercises and checkpoints easier to reason about.

package main

import (
	"fmt"
	"sort"
)

// Walk through one fixed scenario so maps and frequency counting behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key maps and frequency counting path.
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

	// Report values so learners can verify the maps and frequency counting outcome.
	fmt.Println("Character frequencies:")
	for _, key := range keys {
		fmt.Printf("%c -> %d\n", key, frequencies[key])
	}
}
