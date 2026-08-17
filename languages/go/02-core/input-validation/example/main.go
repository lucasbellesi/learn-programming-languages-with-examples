// Module focus: Rejecting invalid input before the main workflow continues.
// Why it matters: the example makes it possible to reject malformed and out-of-domain input
// without corrupting state before the learner tackles the exercises.

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Separate helpers keep the main path focused on how to reject malformed and out-of-domain input
// without corrupting state.
func readRequiredLine(reader *bufio.Reader, prompt string) string {
	for {
		fmt.Print(prompt)
		line, err := reader.ReadString('\n')
		if err == nil || len(line) > 0 {
			return strings.TrimSpace(line)
		}

		fmt.Println("Input error. Please try again.")
	}
}

func readIntInRange(reader *bufio.Reader, prompt string, minValue int, maxValue int) int {
	for {
		// Parse first, then validate the numeric range.
		value, parseErr := strconv.Atoi(readRequiredLine(reader, prompt))
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
		// The same validation shape works for decimal input too.
		value, parseErr := strconv.ParseFloat(readRequiredLine(reader, prompt), 64)
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

// Fixed inputs make the consequence of assuming `Atoi` and `ParseFloat` always succeed visible
// and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	reader := bufio.NewReader(os.Stdin)

	age := readIntInRange(reader, "Enter your age (1-120): ", 1, 120)
	gpa := readFloatInRange(reader, "Enter your GPA (0.0-4.0): ", 0.0, 4.0)

	// The printed result shows whether the program can design retry and termination behavior that
	// cannot loop accidentally.
	fmt.Println("\nValidated input summary:")
	fmt.Printf("Age: %d\n", age)
	fmt.Printf("GPA: %.2f\n", gpa)
}
