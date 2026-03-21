// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

func parseScoreRow(line string) (string, int, bool) {
	// Intent: keep row parsing logic isolated so the main flow is easy to follow.
	parts := strings.Fields(line)
	// Intent: guard malformed rows before attempting integer conversion.
	if len(parts) != 2 {
		return "", 0, false
	}

	score, err := strconv.Atoi(parts[1])
	if err != nil {
		return "", 0, false
	}

	return parts[0], score, true
}

func main() {
	// Program flow: prepare input, parse rows, then generate a summary file.
	runDirectory := filepath.Clean(filepath.Join(os.TempDir(), "learn-lang-file-io-go"))
	if err := os.MkdirAll(runDirectory, 0o755); err != nil {
		fmt.Println("Could not create temp directory.")
		return
	}

	inputPath := filepath.Join(runDirectory, "scores.txt")
	outputPath := filepath.Join(runDirectory, "summary.txt")

	if _, err := os.Stat(inputPath); err != nil {
		sample := strings.Join([]string{"ana 90", "bob 82", "invalid row", "carla 95"}, "\n") + "\n"
		if writeErr := os.WriteFile(inputPath, []byte(sample), 0o644); writeErr != nil {
			fmt.Println("Could not create sample input file.")
			return
		}
	}

	file, err := os.Open(inputPath)
	if err != nil {
		fmt.Printf("Could not open %s\n", inputPath)
		return
	}
	defer file.Close()

	validRows := 0
	sum := 0
	scanner := bufio.NewScanner(file)

	// Intent: iterate through file rows in a deterministic order.
	for scanner.Scan() {
		line := scanner.Text()
		name, score, ok := parseScoreRow(line)
		if !ok {
			continue
		}

		validRows++
		sum += score
		// Intent: print parsed rows so learners can verify intermediate state.
		fmt.Printf("%s -> %d\n", name, score)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Could not read input file.")
		return
	}

	if validRows == 0 {
		fmt.Println("No valid rows found.")
		return
	}

	average := float64(sum) / float64(validRows)
	summary := fmt.Sprintf("Rows: %d\nAverage: %.2f\n", validRows, average)
	if err := os.WriteFile(outputPath, []byte(summary), 0o644); err != nil {
		fmt.Printf("Could not create %s\n", outputPath)
		return
	}

	fmt.Printf("Summary written to %s\n", outputPath)
}
