// Module focus: Counting repeated values and summarizing them through keyed lookups.
// Why it matters: the example makes it possible to use key-value collections to aggregate and
// retrieve data before the learner tackles the exercises.

package main

import (
	"fmt"
	"sort"
)

// Fixed inputs make the consequence of reading missing keys without understanding zero-value
// defaults visible and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
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

	// The printed result shows whether the program can define normalization and missing-key behavior
	// explicitly.
	fmt.Println("Character frequencies:")
	for _, key := range keys {
		fmt.Printf("%c -> %d\n", key, frequencies[key])
	}
}
