// Module focus: Reading plain-text files, parsing rows, and writing clear results.
// Why it matters: practicing file io basics patterns makes exercises and checkpoints easier to reason about.

package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	// Explicit arguments make missing input observable instead of creating it silently.
	inputPath := filepath.Join("example", "fixtures", "scores.txt")
	outputPath := filepath.Join("build", "report.txt")
	if len(os.Args) > 1 {
		inputPath = os.Args[1]
	}
	if len(os.Args) > 2 {
		outputPath = os.Args[2]
	}

	file, err := os.Open(inputPath)
	if err != nil {
		fmt.Printf("Could not open %s: %v\n", inputPath, err)
		return
	}
	defer file.Close()

	// Keep accepted and rejected records separate so the report can explain both.
	var records []scoreRecord
	invalidRows := 0
	// Blank lines are formatting noise; malformed non-blank rows count as rejected data.
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		if strings.TrimSpace(scanner.Text()) == "" {
			continue
		}
		record, ok := parseScoreRow(scanner.Text())
		if ok {
			records = append(records, record)
		} else {
			invalidRows++
		}
	}
	if err := scanner.Err(); err != nil {
		fmt.Printf("Could not read input file: %v\n", err)
		return
	}

	// Build and persist one deterministic learner-visible report.
	report := buildReport(records, invalidRows)
	if err := os.MkdirAll(filepath.Dir(outputPath), 0o755); err != nil {
		fmt.Printf("Could not create output directory: %v\n", err)
		return
	}
	if err := os.WriteFile(outputPath, []byte(report+"\n"), 0o644); err != nil {
		fmt.Printf("Could not create %s: %v\n", outputPath, err)
		return
	}

	// Print the same report so file and console results are easy to compare.
	// The explicit path also tells learners exactly where the generated artifact lives.
	fmt.Printf("Report file: %s\n", outputPath)
	fmt.Println(report)
}
