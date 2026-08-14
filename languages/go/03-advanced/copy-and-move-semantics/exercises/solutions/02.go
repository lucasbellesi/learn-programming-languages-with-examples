package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Print("How many strings? ")
	if !scanner.Scan() {
		fmt.Println("Please enter a positive count.")
		return
	}

	var count int
	if _, err := fmt.Sscanf(scanner.Text(), "%d", &count); err != nil || count <= 0 {
		fmt.Println("Please enter a positive count.")
		return
	}

	values := make([]string, 0, count)

	for i := 0; i < count; i++ {
		fmt.Printf("String %d: ", i+1)
		if !scanner.Scan() {
			break
		}

		input := strings.TrimSpace(scanner.Text())
		values = append(values, input)

		alias := values
		snapshot := append([]string(nil), values...)

		fmt.Printf("Current size: %d\n", len(values))
		fmt.Printf("Alias sees size: %d\n", len(alias))
		fmt.Printf("Snapshot size: %d\n", len(snapshot))
	}
}
