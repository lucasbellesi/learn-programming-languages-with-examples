// This extra example extends input validation with a menu choice validator.
// Example purpose: keep prompting until the user enters a valid option and quantity.

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readMenuChoice(reader *bufio.Reader) string {
	for {
		fmt.Print("Choose [1] Add, [2] Remove, [3] Exit: ")
		raw, _ := reader.ReadString('\n')
		choice := strings.TrimSpace(raw)
		if choice == "1" || choice == "2" || choice == "3" {
			return choice
		}
		fmt.Println("Option must be 1, 2, or 3.")
	}
}

func readQuantity(reader *bufio.Reader) int {
	for {
		fmt.Print("Enter quantity (1-9): ")
		raw, _ := reader.ReadString('\n')
		value, err := strconv.Atoi(strings.TrimSpace(raw))
		if err != nil {
			fmt.Println("Quantity must be an integer.")
			continue
		}
		if value >= 1 && value <= 9 {
			return value
		}
		fmt.Println("Quantity must be between 1 and 9.")
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	choice := readMenuChoice(reader)
	if choice == "3" {
		fmt.Println("Nothing to process.")
		return
	}

	quantity := readQuantity(reader)
	action := "added"
	if choice == "2" {
		action = "removed"
	}
	fmt.Printf("%d item(s) %s.\n", quantity, action)
}
