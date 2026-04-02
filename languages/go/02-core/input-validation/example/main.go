// Module focus: Rejecting invalid input before the main workflow continues.
// Why it matters: practicing input validation patterns makes exercises and checkpoints easier to reason about.

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Helper setup for input validation; this keeps the walkthrough readable.
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
			fmt.Println("Invalid input type. Please enter an integer.")
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
			fmt.Println("Invalid input type. Please enter a decimal number.")
			continue
		}

		if value < minValue || value > maxValue {
			fmt.Printf("Value must be between %.1f and %.1f.\n", minValue, maxValue)
			continue
		}

		return value
	}
}

// Walk through one fixed scenario so input validation behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key input validation path.
	reader := bufio.NewReader(os.Stdin)

	age := readIntInRange(reader, "Enter your age (1-120): ", 1, 120)
	gpa := readFloatInRange(reader, "Enter your GPA (0.0-4.0): ", 0.0, 4.0)

	// Report values so learners can verify the input validation outcome.
	fmt.Println("\nValidated input summary:")
	fmt.Printf("Age: %d\n", age)
	fmt.Printf("GPA: %.2f\n", gpa)
}
