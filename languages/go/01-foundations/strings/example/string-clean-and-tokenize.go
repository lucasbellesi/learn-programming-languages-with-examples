// This helper example focuses on isolating string cleanup before the main example combines the steps.

// This extra example extends strings with text normalization and token extraction.

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter a sentence: ")
	line, err := reader.ReadString('\n')
	if err != nil && len(line) == 0 {
		fmt.Println("Could not read the sentence.")
		return
	}
	line = strings.TrimRight(line, "\r\n")

	cleanedRunes := make([]rune, 0, len(line))
	for _, char := range line {
		if unicode.IsLetter(char) || unicode.IsDigit(char) {
			cleanedRunes = append(cleanedRunes, unicode.ToLower(char))
		} else {
			cleanedRunes = append(cleanedRunes, ' ')
		}
	}

	cleaned := string(cleanedRunes)
	words := strings.Fields(cleaned)

	fmt.Printf("Normalized text: %s\n", cleaned)
	fmt.Printf("Tokens (%d):\n", len(words))
	for _, word := range words {
		fmt.Printf("- %s\n", word)
	}
}
