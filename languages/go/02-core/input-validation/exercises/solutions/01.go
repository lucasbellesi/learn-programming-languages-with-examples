package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readIntInRange(reader *bufio.Reader, prompt string, minValue int, maxValue int) int {
	for {
		fmt.Print(prompt)
		line, err := reader.ReadString('\n')
		if err != nil && len(line) == 0 {
			fmt.Println("Input error. Please try again.")
			continue
		}

		value, parseErr := strconv.Atoi(strings.TrimSpace(line))
		if parseErr != nil {
			fmt.Println("Invalid input. Please enter an integer.")
			continue
		}

		if value < minValue || value > maxValue {
			fmt.Println("Out of range. Try again.")
			continue
		}

		return value
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	value := readIntInRange(reader, "Enter an integer from 1 to 100: ", 1, 100)
	fmt.Printf("Square: %d\n", value*value)
}
