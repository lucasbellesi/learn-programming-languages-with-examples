package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Student struct {
	Name  string
	Score int
}

func readPositiveCount(scanner *bufio.Scanner) int {
	for {
		fmt.Print("How many students? ")
		if !scanner.Scan() {
			continue
		}

		count, err := strconv.Atoi(strings.TrimSpace(scanner.Text()))
		if err != nil {
			fmt.Println("Invalid number. Try again.")
			continue
		}
		if count <= 0 {
			fmt.Println("Please enter a positive number.")
			continue
		}

		return count
	}
}

func readScore(scanner *bufio.Scanner, studentName string) int {
	for {
		fmt.Printf("Score for %s (0-100): ", studentName)
		if !scanner.Scan() {
			continue
		}

		score, err := strconv.Atoi(strings.TrimSpace(scanner.Text()))
		if err != nil {
			fmt.Println("Invalid score. Enter a number from 0 to 100.")
			continue
		}
		if score < 0 || score > 100 {
			fmt.Println("Score out of range. Enter a value from 0 to 100.")
			continue
		}

		return score
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	count := readPositiveCount(scanner)
	students := make([]Student, 0, count)

	for index := 0; index < count; index++ {
		fmt.Printf("Student name %d: ", index+1)
		scanner.Scan()
		name := scanner.Text()
		score := readScore(scanner, name)
		students = append(students, Student{Name: name, Score: score})
	}

	minScore := students[0].Score
	maxScore := students[0].Score
	sum := 0

	fmt.Println()
	fmt.Println("Students:")
	for _, student := range students {
		fmt.Printf("- %s: %d\n", student.Name, student.Score)
		sum += student.Score
		if student.Score < minScore {
			minScore = student.Score
		}
		if student.Score > maxScore {
			maxScore = student.Score
		}
	}

	average := float64(sum) / float64(len(students))
	fmt.Printf("Average: %v\n", average)
	fmt.Printf("Minimum: %d\n", minScore)
	fmt.Printf("Maximum: %d\n", maxScore)
}
