// Module focus: Cleaning and combining text while preserving readable string logic.
// Why it matters: the example makes it possible to normalize, inspect, and transform textual data
// before the learner tackles the exercises.

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

// Fixed inputs make the consequence of counting words without removing extra spaces visible and
// repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	reader := bufio.NewReader(os.Stdin)
	// The printed result shows whether the program can handle empty input and character boundaries
	// safely.
	fmt.Print("Enter a sentence: ")
	line, _ := reader.ReadString('\n')

	var builder strings.Builder
	for _, ch := range line {
		if unicode.IsLetter(ch) || unicode.IsDigit(ch) {
			builder.WriteRune(unicode.ToLower(ch))
		} else {
			builder.WriteRune(' ')
		}
	}

	cleaned := builder.String()
	words := strings.Fields(cleaned)

	fmt.Printf("Normalized text: %s\n", cleaned)
	fmt.Printf("Tokens (%d):\n", len(words))
	for _, word := range words {
		fmt.Printf("- %s\n", word)
	}
}
