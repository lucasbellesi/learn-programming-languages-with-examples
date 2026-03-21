package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
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
