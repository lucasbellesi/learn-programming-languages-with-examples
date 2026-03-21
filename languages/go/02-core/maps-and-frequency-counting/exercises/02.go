package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Enter text: ")
	text, _ := reader.ReadString('\n')
	text = strings.TrimRight(text, "\r\n")

	frequency := make(map[rune]int)
	for _, ch := range text {
		frequency[ch]++
	}

	result := rune(0)
	for _, ch := range text {
		if frequency[ch] == 1 {
			result = ch
			break
		}
	}

	if result == rune(0) {
		fmt.Println("No non-repeating character found.")
	} else {
		fmt.Printf("First non-repeating character: %c\n", result)
	}
}
