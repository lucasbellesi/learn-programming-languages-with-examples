// Module focus: Cleaning and combining text while preserving readable string logic.
// Why it matters: practicing strings patterns makes exercises and checkpoints easier to reason about.

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

// Walk through one fixed scenario so strings behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key strings path.
	reader := bufio.NewReader(os.Stdin)
	// Report values so learners can verify the strings outcome.
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
