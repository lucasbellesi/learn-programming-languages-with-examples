// This example shows cleaning and combining text while preserving readable string logic.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

// Run one deterministic scenario so the console output makes cleaning and combining text while preserving readable string logic easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	reader := bufio.NewReader(os.Stdin)
	// Print the observed state here so learners can connect the code path to a concrete result.
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
