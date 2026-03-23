package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func bucketForScore(score int) int {
	if score == 100 {
		return 9
	}
	return score / 10
}

func writeLineBoth(writer *bufio.Writer, line string) {
	fmt.Println(line)
	fmt.Fprintln(writer, line)
}

func main() {
	file, err := os.Create("core_assessment_report.txt")
	if err != nil {
		fmt.Println("Could not create report file.")
		return
	}
	defer file.Close()

	writer := bufio.NewWriter(file)
	defer writer.Flush()

	values := make([]int, 0)
	buckets := make([]int, 10)

	fmt.Println("Enter integer values (0-100). End with -1.")
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		text := strings.TrimSpace(scanner.Text())
		value, parseErr := strconv.Atoi(text)
		if parseErr != nil {
			fmt.Println("Invalid input. Stopping read.")
			break
		}

		if value == -1 {
			break
		}
		if value < 0 || value > 100 {
			fmt.Printf("Ignoring out-of-range value: %d\n", value)
			continue
		}

		values = append(values, value)
		buckets[bucketForScore(value)]++
	}

	if len(values) == 0 {
		writeLineBoth(writer, "No valid values were entered.")
		writeLineBoth(writer, "Report saved to core_assessment_report.txt")
		return
	}

	minValue := values[0]
	maxValue := values[0]
	sum := 0
	for _, value := range values {
		sum += value
		if value < minValue {
			minValue = value
		}
		if value > maxValue {
			maxValue = value
		}
	}

	average := float64(sum) / float64(len(values))
	writeLineBoth(writer, fmt.Sprintf("Valid count: %d", len(values)))
	writeLineBoth(writer, fmt.Sprintf("Minimum: %d", minValue))
	writeLineBoth(writer, fmt.Sprintf("Maximum: %d", maxValue))
	writeLineBoth(writer, fmt.Sprintf("Average: %v", average))
	writeLineBoth(writer, "Frequency table:")

	for index := 0; index < 10; index++ {
		start := index * 10
		end := start + 9
		if index == 9 {
			end = 100
		}
		writeLineBoth(writer, fmt.Sprintf("%d-%d: %d", start, end, buckets[index]))
	}

	writeLineBoth(writer, "Report saved to core_assessment_report.txt")
}
