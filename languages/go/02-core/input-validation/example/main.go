// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readIntInRange(reader *bufio.Reader, prompt string, minValue int, maxValue int) int {
	// Intent: iterate through data in a clear and deterministic order.
	for {
		// Intent: print intermediate or final output for quick behavior verification.
		fmt.Print(prompt)
		// Intent: gather typed input first so later operations are predictable.
		line, err := reader.ReadString('\n')
		// Intent: guard invalid or edge-case paths before the main path continues.
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

func main() {
	// Program flow: collect input, apply core logic, then print a verifiable result.
	reader := bufio.NewReader(os.Stdin)

	age := readIntInRange(reader, "Enter your age (1-120): ", 1, 120)
	gpa := readFloatInRange(reader, "Enter your GPA (0.0-4.0): ", 0.0, 4.0)

	fmt.Println("\nValidated input summary:")
	fmt.Printf("Age: %d\n", age)
	fmt.Printf("GPA: %.2f\n", gpa)
}
