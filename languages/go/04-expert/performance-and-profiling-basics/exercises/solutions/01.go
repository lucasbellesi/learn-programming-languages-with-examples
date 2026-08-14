package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Line count: ")
	line, _ := reader.ReadString('\n')
	lineCount, err := strconv.Atoi(strings.TrimSpace(line))
	if err != nil {
		fmt.Println("Invalid line count.")
		return
	}
	if lineCount < 0 {
		fmt.Println("Line count cannot be negative.")
		return
	}

	concatDuration := measure(func() { _ = buildWithConcatenation(lineCount) })
	builderDuration := measure(func() { _ = buildWithBuilder(lineCount) })
	fmt.Printf("Concatenation: %v\n", concatDuration)
	fmt.Printf("Builder: %v\n", builderDuration)
}

func measure(action func()) time.Duration {
	start := time.Now()
	action()
	return time.Since(start)
}

func buildWithConcatenation(lineCount int) string {
	result := ""
	for index := 0; index < lineCount; index++ {
		result += fmt.Sprintf("item-%d;", index)
	}
	return result
}

func buildWithBuilder(lineCount int) string {
	var builder strings.Builder
	builder.Grow(lineCount * 8)
	for index := 0; index < lineCount; index++ {
		fmt.Fprintf(&builder, "item-%d;", index)
	}
	return builder.String()
}
