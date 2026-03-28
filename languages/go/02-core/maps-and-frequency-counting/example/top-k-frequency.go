// This extra example extends maps-and-frequency-counting with ranked frequency output.
// Example purpose: count repeated words, then sort by frequency and name.

package main

import (
	"fmt"
	"sort"
)

type frequencyItem struct {
	word  string
	count int
}

func main() {
	var count int
	fmt.Print("How many words? ")
	if _, err := fmt.Scan(&count); err != nil || count <= 0 {
		fmt.Println("Please enter a positive number.")
		return
	}

	frequency := make(map[string]int)
	for index := 0; index < count; index++ {
		var word string
		fmt.Printf("Word %d: ", index+1)
		if _, err := fmt.Scan(&word); err != nil {
			fmt.Println("Please enter a valid word.")
			return
		}
		frequency[word]++
	}

	var k int
	fmt.Print("How many top words to show? ")
	if _, err := fmt.Scan(&k); err != nil || k <= 0 {
		fmt.Println("Please enter a positive value for k.")
		return
	}

	items := make([]frequencyItem, 0, len(frequency))
	for word, wordCount := range frequency {
		items = append(items, frequencyItem{word: word, count: wordCount})
	}

	sort.Slice(items, func(left int, right int) bool {
		if items[left].count != items[right].count {
			return items[left].count > items[right].count
		}
		return items[left].word < items[right].word
	})

	if k > len(items) {
		k = len(items)
	}

	fmt.Printf("\nTop %d words:\n", k)
	for index := 0; index < k; index++ {
		fmt.Printf("%d. %s -> %d\n", index+1, items[index].word, items[index].count)
	}
}
