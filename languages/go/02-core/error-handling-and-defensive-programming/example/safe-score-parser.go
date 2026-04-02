// This helper example focuses on isolating the parsing guard so invalid text never silently becomes a score.

// This extra example extends defensive programming with safe score parsing.

package main

import (
	"fmt"
	"strconv"
	"strings"
)

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
func tryParseRow(row string) (string, int, bool) {
	parts := strings.Split(row, ":")
	if len(parts) != 2 {
		return "", 0, false
	}

	name := strings.TrimSpace(parts[0])
	if name == "" {
		return "", 0, false
	}

	score, err := strconv.Atoi(strings.TrimSpace(parts[1]))
	if err != nil || score < 0 || score > 100 {
		return "", 0, false
	}

	return name, score, true
}

func main() {
	rows := []string{"Ana: 91", "InvalidRow", "Bruno: not-a-number", "Carla: 77", "Diego: 130"}
	validRows := make([]string, 0)

	for _, row := range rows {
		name, score, ok := tryParseRow(row)
		if !ok {
			fmt.Printf("Skipping invalid row: %s\n", row)
			continue
		}

		validRows = append(validRows, fmt.Sprintf("- %s => %d", name, score))
	}

	fmt.Printf("Valid rows: %d\n", len(validRows))
	for _, row := range validRows {
		fmt.Println(row)
	}
}
