// This example shows measuring hot paths before changing code for speed.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import (
	"fmt"
	"strings"
	"time"
)

// Define the reusable pieces first so the main flow can focus on one observable scenario.
var (
	retainedText   string
	retainedValues []int
)

// Run one deterministic scenario so the console output makes measuring hot paths before changing code for speed easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	const lineCount = 4000
	const repetitions = 12
	concatDuration := measureAverage(func() { retainedText = buildWithConcatenation(lineCount) }, repetitions)
	builderDuration := measureAverage(func() { retainedText = buildWithBuilder(lineCount) }, repetitions)

	// Print the observed state here so learners can connect the code path to a concrete result.
	fmt.Printf("Average string concatenation (%d runs): %v\n", repetitions, concatDuration)
	fmt.Printf("Average strings.Builder (%d runs): %v\n", repetitions, builderDuration)

	const itemCount = 200000
	noCapacity := measureAverage(func() { retainedValues = fillWithoutCapacity(itemCount) }, repetitions)
	withCapacity := measureAverage(func() { retainedValues = fillWithCapacity(itemCount) }, repetitions)

	fmt.Printf("Average slice fill without capacity (%d runs): %v\n", repetitions, noCapacity)
	fmt.Printf("Average slice fill with capacity (%d runs): %v\n", repetitions, withCapacity)
}

func measureAverage(action func(), repetitions int) time.Duration {
	action()

	var total time.Duration
	for iteration := 0; iteration < repetitions; iteration++ {
		start := time.Now()
		action()
		total += time.Since(start)
	}
	return total / time.Duration(repetitions)
}

func buildWithConcatenation(lineCount int) string {
	result := ""
	for index := 0; index < lineCount; index++ {
		result += fmt.Sprintf("row-%d;", index)
	}
	return result
}

func buildWithBuilder(lineCount int) string {
	var builder strings.Builder
	builder.Grow(lineCount * 8)
	for index := 0; index < lineCount; index++ {
		fmt.Fprintf(&builder, "row-%d;", index)
	}
	return builder.String()
}

func fillWithoutCapacity(itemCount int) []int {
	values := []int{}
	for index := 0; index < itemCount; index++ {
		values = append(values, index)
	}
	return values
}

func fillWithCapacity(itemCount int) []int {
	values := make([]int, 0, itemCount)
	for index := 0; index < itemCount; index++ {
		values = append(values, index)
	}
	return values
}
