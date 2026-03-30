// Example purpose: compare a couple of small optimization choices with simple timings.

package main

import (
	"fmt"
	"strings"
	"time"
)

var (
	retainedText   string
	retainedValues []int
)

func main() {
	// Program flow: measure two paired implementations on the same workload size.
	const lineCount = 4000
	const repetitions = 12
	concatDuration := measureAverage(func() { retainedText = buildWithConcatenation(lineCount) }, repetitions)
	builderDuration := measureAverage(func() { retainedText = buildWithBuilder(lineCount) }, repetitions)

	fmt.Printf("Average string concatenation (%d runs): %v\n", repetitions, concatDuration)
	fmt.Printf("Average strings.Builder (%d runs): %v\n", repetitions, builderDuration)

	const itemCount = 200000
	noCapacity := measureAverage(func() { retainedValues = fillWithoutCapacity(itemCount) }, repetitions)
	withCapacity := measureAverage(func() { retainedValues = fillWithCapacity(itemCount) }, repetitions)

	// Intent: final output keeps the comparison direct and easy to verify.
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
