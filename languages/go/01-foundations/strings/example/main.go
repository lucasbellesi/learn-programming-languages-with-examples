// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

func main() {
	// Program flow: collect input, apply core logic, then print a verifiable result.
	reader := bufio.NewReader(os.Stdin)
	// Intent: print intermediate or final output for quick behavior verification.
	fmt.Print("Enter a sentence: ")
	// Intent: gather typed input first so later operations are predictable.
	line, _ := reader.ReadString('\n')

	var builder strings.Builder
	// Intent: iterate through data in a clear and deterministic order.
	for _, ch := range line {
		// Intent: guard invalid or edge-case paths before the main path continues.
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
