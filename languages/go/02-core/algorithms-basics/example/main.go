package main

import "fmt"

func linearSearch(values []int, target int) int {
	for index, value := range values {
		if value == target {
			return index
		}
	}
	return -1
}

func countOccurrences(values []int, target int) int {
	count := 0
	for _, value := range values {
		if value == target {
			count++
		}
	}
	return count
}

func minMax(values []int) (int, int, bool) {
	if len(values) == 0 {
		return 0, 0, false
	}

	minValue := values[0]
	maxValue := values[0]
	for _, value := range values {
		if value < minValue {
			minValue = value
		}
		if value > maxValue {
			maxValue = value
		}
	}

	return minValue, maxValue, true
}

func main() {
	values := []int{4, 7, 4, 1, 9, 4, 2}
	target := 4

	firstIndex := linearSearch(values, target)
	fmt.Printf("First index of %d: %d\n", target, firstIndex)
	fmt.Printf("Occurrences of %d: %d\n", target, countOccurrences(values, target))

	minValue, maxValue, ok := minMax(values)
	if !ok {
		fmt.Println("No values to process.")
		return
	}

	fmt.Printf("Minimum: %d\n", minValue)
	fmt.Printf("Maximum: %d\n", maxValue)
}
