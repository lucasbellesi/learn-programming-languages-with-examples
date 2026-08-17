// Module focus: Measuring hot paths before changing code for speed.
// Why it matters: the example makes it possible to measure before optimizing and interpret timing
// data cautiously before the learner tackles the exercises.

package main

import (
	"fmt"
	"strings"
	"time"
)

// Separate helpers keep the main path focused on how to measure before optimizing and interpret
// timing data cautiously.
var (
	retainedText   string
	retainedValues []int
)

// Fixed inputs make the consequence of timing workloads that are too small to compare fairly
// visible and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	const lineCount = 4000
	const repetitions = 12
	// Measure two implementations of the same string-building task.
	concatDuration := measureAverage(func() { retainedText = buildWithConcatenation(lineCount) }, repetitions)
	builderDuration := measureAverage(func() { retainedText = buildWithBuilder(lineCount) }, repetitions)

	// The printed result shows whether the program can relate algorithmic and allocation choices to
	// observed cost.
	fmt.Printf("Average string concatenation (%d runs): %v\n", repetitions, concatDuration)
	fmt.Printf("Average strings.Builder (%d runs): %v\n", repetitions, builderDuration)

	const itemCount = 200000
	// Repeat the measurement pattern for slice growth with and without preallocation.
	noCapacity := measureAverage(func() { retainedValues = fillWithoutCapacity(itemCount) }, repetitions)
	withCapacity := measureAverage(func() { retainedValues = fillWithCapacity(itemCount) }, repetitions)

	fmt.Printf("Average slice fill without capacity (%d runs): %v\n", repetitions, noCapacity)
	fmt.Printf("Average slice fill with capacity (%d runs): %v\n", repetitions, withCapacity)
}

func measureAverage(action func(), repetitions int) time.Duration {
	// Warm up once so setup cost is less likely to dominate the repeated samples.
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
	// Grow communicates expected size and reduces repeated allocation work.
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
