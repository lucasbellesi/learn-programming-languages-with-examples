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
	fmt.Print("Enter text: ")
	line, _ := reader.ReadString('\n')

	normalized := make([]rune, 0)
	for _, ch := range strings.ToLower(line) {
		if unicode.IsLetter(ch) {
			normalized = append(normalized, ch)
		}
	}

	if len(normalized) == 0 {
		fmt.Println("No letters to evaluate.")
		return
	}

	left := 0
	right := len(normalized) - 1
	isPalindrome := true

	for left < right {
		if normalized[left] != normalized[right] {
			isPalindrome = false
			break
		}
		left++
		right--
	}

	if isPalindrome {
		fmt.Println("Palindrome")
	} else {
		fmt.Println("Not palindrome")
	}
}
