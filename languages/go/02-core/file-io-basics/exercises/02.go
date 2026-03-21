package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parseScoreRow(line string) (int, bool) {
	parts := strings.Fields(line)
	if len(parts) != 2 {
		return 0, false
	}

	score, err := strconv.Atoi(parts[1])
	if err != nil {
		return 0, false
	}

	return score, true
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Enter file path (name score rows): ")
	path, _ := reader.ReadString('\n')
	path = strings.TrimSpace(path)

	file, err := os.Open(path)
	if err != nil {
		fmt.Println("Could not open file.")
		return
	}
	defer file.Close()

	validRows := 0
	invalidRows := 0
	sum := 0

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		score, ok := parseScoreRow(scanner.Text())
		if ok {
			validRows++
			sum += score
		} else {
			invalidRows++
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("File processing failed.")
		return
	}

	fmt.Printf("Valid rows: %d\n", validRows)
	fmt.Printf("Invalid rows: %d\n", invalidRows)

	if validRows > 0 {
		average := float64(sum) / float64(validRows)
		fmt.Printf("Average score: %.2f\n", average)
	} else {
		fmt.Println("No valid rows found.")
	}
}
