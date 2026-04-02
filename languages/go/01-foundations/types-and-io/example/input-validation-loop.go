// This helper example focuses on focusing on the retry loop so invalid input handling is easy to trace.

// This extra example extends types-and-io with a validation loop.

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Enter your full name: ")
	fullName, err := reader.ReadString('\n')
	if err != nil && len(fullName) == 0 {
		fmt.Println("Could not read the full name.")
		return
	}
	fullName = strings.TrimSpace(fullName)

	var age int
	for {
		fmt.Print("Enter your age (1-120): ")
		rawAge, readErr := reader.ReadString('\n')
		if readErr != nil && len(rawAge) == 0 {
			fmt.Println("Invalid input. Please enter a number.")
			continue
		}

		parsedAge, parseErr := strconv.Atoi(strings.TrimSpace(rawAge))
		if parseErr != nil {
			fmt.Println("Invalid input. Please enter a number.")
			continue
		}
		if parsedAge < 1 || parsedAge > 120 {
			fmt.Println("Age must be between 1 and 120.")
			continue
		}

		age = parsedAge
		break
	}

	fmt.Println("\nRegistration summary:")
	fmt.Printf("Name: %s\n", fullName)
	fmt.Printf("Age: %d\n", age)
}
