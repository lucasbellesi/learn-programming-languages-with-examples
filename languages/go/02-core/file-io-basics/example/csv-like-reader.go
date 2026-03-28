// This extra example extends file-io-basics with line parsing and validation.
// Example purpose: read simple name,score rows from a text file.

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type studentScore struct {
	name  string
	score int
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("CSV-like input file path (name,score): ")
	path, err := reader.ReadString('\n')
	if err != nil && len(path) == 0 {
		fmt.Println("Could not read the file path.")
		return
	}
	path = strings.TrimSpace(path)

	handle, openErr := os.Open(path)
	if openErr != nil {
		fmt.Printf("Could not open file: %s\n", path)
		return
	}
	defer handle.Close()

	rows := make([]studentScore, 0)
	scanner := bufio.NewScanner(handle)
	lineNumber := 0

	for scanner.Scan() {
		lineNumber++
		line := strings.TrimSpace(scanner.Text())
		if line == "" {
			continue
		}

		parts := strings.SplitN(line, ",", 2)
		if len(parts) != 2 {
			fmt.Printf("Skipping malformed line %d: %s\n", lineNumber, line)
			continue
		}

		score, parseErr := strconv.Atoi(strings.TrimSpace(parts[1]))
		if parseErr != nil || score < 0 || score > 100 {
			fmt.Printf("Skipping invalid score on line %d: %s\n", lineNumber, parts[1])
			continue
		}

		rows = append(rows, studentScore{name: parts[0], score: score})
	}

	fmt.Printf("\nValid rows: %d\n", len(rows))
	for _, row := range rows {
		fmt.Printf("- %s: %d\n", row.name, row.score)
	}
}
