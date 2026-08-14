package main

import (
	"fmt"
	"strings"
)

func countVowels(text string) int {
	vowels := "aeiou"
	count := 0

	for _, ch := range strings.ToLower(text) {
		if strings.ContainsRune(vowels, ch) {
			count++
		}
	}

	return count
}

func main() {
	var line string
	fmt.Print("Enter text: ")
	fmt.Scanln(&line)

	fmt.Printf("Number of vowels: %d\n", countVowels(line))
}
