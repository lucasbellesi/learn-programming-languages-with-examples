// Example purpose: compare a couple of small optimization choices with simple timings.

package main

import (
	"fmt"
	"strings"
	"time"
)

func main() {
	// Program flow: measure two paired implementations on the same workload size.
	const lineCount = 4000
	concatDuration := measure(func() { _ = buildWithConcatenation(lineCount) })
	builderDuration := measure(func() { _ = buildWithBuilder(lineCount) })

	fmt.Printf("String concatenation: %v\n", concatDuration)
	fmt.Printf("strings.Builder: %v\n", builderDuration)

	const itemCount = 200000
	noCapacity := measure(func() { _ = fillWithoutCapacity(itemCount) })
	withCapacity := measure(func() { _ = fillWithCapacity(itemCount) })

	// Intent: final output keeps the comparison direct and easy to verify.
	fmt.Printf("Slice fill without capacity: %v\n", noCapacity)
	fmt.Printf("Slice fill with capacity: %v\n", withCapacity)
}

func measure(action func()) time.Duration {
	start := time.Now()
	action()
	return time.Since(start)
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
