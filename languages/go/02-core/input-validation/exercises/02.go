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
			fmt.Printf("Value must be between %d and %d.\n", minValue, maxValue)
			continue
		}

		return value
	}
}

func readFloatInRange(reader *bufio.Reader, prompt string, minValue float64, maxValue float64) float64 {
	for {
		fmt.Print(prompt)
		line, err := reader.ReadString('\n')
		if err != nil && len(line) == 0 {
			fmt.Println("Input error. Please try again.")
			continue
		}

		value, parseErr := strconv.ParseFloat(strings.TrimSpace(line), 64)
		if parseErr != nil {
			fmt.Println("Invalid input. Please enter a number.")
			continue
		}

		if value < minValue || value > maxValue {
			fmt.Printf("Value must be between %.1f and %.1f.\n", minValue, maxValue)
			continue
		}

		return value
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	count := readIntInRange(reader, "How many scores (1-50)? ", 1, 50)

	sum := 0.0
	for i := 0; i < count; i++ {
		score := readFloatInRange(reader, fmt.Sprintf("Score %d (0-100): ", i+1), 0.0, 100.0)
		sum += score
	}

	fmt.Printf("Average score: %.2f\n", sum/float64(count))
}
