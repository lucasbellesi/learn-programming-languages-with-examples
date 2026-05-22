// Module focus: Reading plain-text files, parsing rows, and writing clear results.
// Why it matters: practicing file io basics patterns makes exercises and checkpoints easier to reason about.

package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

// Helper setup for file io basics; this keeps the walkthrough readable.
func parseScoreRow(line string) (string, int, bool) {
	// Each valid row has one name token followed by one integer score.
	parts := strings.Fields(line)
	if len(parts) != 2 {
		return "", 0, false
	}

	score, err := strconv.Atoi(parts[1])
	return parts[0], score, err == nil
}

// Walk through one fixed scenario so file io basics behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key file io basics path.
	inputPath := filepath.Join(os.TempDir(), "learn-lang-file-io-go-scores.txt")
	outputPath := filepath.Join(os.TempDir(), "learn-lang-file-io-go-summary.txt")
	sample := strings.Join([]string{"ana 90", "bob 82", "invalid row", "carla 95"}, "\n") + "\n"
	if err := os.WriteFile(inputPath, []byte(sample), 0o644); err != nil {
		fmt.Println("Could not create sample input file.")
		return
	}

	// Open the input file, then scan it one learner-visible row at a time.
	file, err := os.Open(inputPath)
	if err != nil {
		fmt.Printf("Could not open %s\n", inputPath)
		return
	}
	defer file.Close()

	validRows, sum := 0, 0
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		name, score, ok := parseScoreRow(scanner.Text())
		if !ok {
			continue
		}

		validRows++
		sum += score
		fmt.Printf("%s -> %d\n", name, score)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Could not read input file.")
		return
	}

	// Summarize only rows that passed parsing, then persist the result.
	average := float64(sum) / float64(validRows)
	summary := fmt.Sprintf("Rows: %d\nAverage: %.2f\n", validRows, average)
	if err := os.WriteFile(outputPath, []byte(summary), 0o644); err != nil {
		fmt.Printf("Could not create %s\n", outputPath)
		return
	}

	// Print the report path so learners can verify the written file.
	fmt.Printf("Summary written to %s\n", outputPath)
}
