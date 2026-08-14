package main

import (
	"fmt"
	"strconv"
	"strings"
)

type scoreRecord struct {
	name  string
	score int
}

func parseScoreRow(line string) (scoreRecord, bool) {
	// Keep parsing independent from file access so malformed rows are easy to test.
	parts := strings.Fields(line)
	if len(parts) < 2 {
		return scoreRecord{}, false
	}
	score, err := strconv.Atoi(parts[len(parts)-1])
	name := strings.Join(parts[:len(parts)-1], " ")
	if err != nil || score < 0 || score > 100 || name == "" {
		return scoreRecord{}, false
	}
	return scoreRecord{name: name, score: score}, true
}

func buildReport(records []scoreRecord, invalidRows int) string {
	lines := []string{
		"Grade Report",
		fmt.Sprintf("Valid records: %d", len(records)),
		fmt.Sprintf("Invalid rows skipped: %d", invalidRows),
	}
	if len(records) == 0 {
		return strings.Join(append(lines, "No valid records."), "\n")
	}

	total := 0
	for _, record := range records {
		total += record.score
	}
	lines = append(lines, fmt.Sprintf("Average: %.2f", float64(total)/float64(len(records))))
	for _, record := range records {
		lines = append(lines, fmt.Sprintf("- %s: %d", record.name, record.score))
	}
	return strings.Join(lines, "\n")
}
