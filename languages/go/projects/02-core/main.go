package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parseRow(line string) (string, int, bool) {
	parts := strings.Fields(line)
	if len(parts) < 2 {
		return "", 0, false
	}

	score, err := strconv.Atoi(parts[len(parts)-1])
	if err != nil {
		return "", 0, false
	}

	name := strings.Join(parts[:len(parts)-1], " ")
	if name == "" {
		return "", 0, false
	}

	return name, score, true
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter input file path: ")
	inputPath, _ := reader.ReadString('\n')
	inputPath = strings.TrimSpace(inputPath)

	file, err := os.Open(inputPath)
	if err != nil {
		fmt.Println("Could not open input file.")
		return
	}
	defer file.Close()

	validRows := 0
	invalidRows := 0
	minScore := 0
	maxScore := 0
	sum := 0

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		_, score, ok := parseRow(scanner.Text())
		if !ok {
			invalidRows++
			continue
		}

		if validRows == 0 {
			minScore = score
			maxScore = score
		} else {
			if score < minScore {
				minScore = score
			}
			if score > maxScore {
				maxScore = score
			}
		}

		sum += score
		validRows++
	}

	report, err := os.Create("report.txt")
	if err != nil {
		fmt.Println("Could not create report.txt")
		return
	}
	defer report.Close()

	fmt.Fprintf(report, "Valid rows: %d\n", validRows)
	fmt.Fprintf(report, "Invalid rows: %d\n", invalidRows)
	if validRows > 0 {
		average := float64(sum) / float64(validRows)
		fmt.Fprintf(report, "Average: %v\n", average)
		fmt.Fprintf(report, "Minimum: %d\n", minScore)
		fmt.Fprintf(report, "Maximum: %d\n", maxScore)
	} else {
		fmt.Fprintln(report, "No valid rows found.")
	}

	fmt.Println("Report generated: report.txt")
}
