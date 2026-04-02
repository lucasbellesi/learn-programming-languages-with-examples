// This example shows reading plain-text files, parsing rows, and writing clear results.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

// Define the reusable pieces first so the main flow can focus on one observable scenario.
func parseScoreRow(line string) (string, int, bool) {
	parts := strings.Fields(line)
	if len(parts) != 2 {
		return "", 0, false
	}

	score, err := strconv.Atoi(parts[1])
	if err != nil {
		return "", 0, false
	}

	return parts[0], score, true
}

// Run one deterministic scenario so the console output makes reading plain-text files, parsing rows, and writing clear results easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	runDirectory := filepath.Clean(filepath.Join(os.TempDir(), "learn-lang-file-io-go"))
	if err := os.MkdirAll(runDirectory, 0o755); err != nil {
		// Print the observed state here so learners can connect the code path to a concrete result.
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

	for scanner.Scan() {
		line := scanner.Text()
		name, score, ok := parseScoreRow(line)
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
