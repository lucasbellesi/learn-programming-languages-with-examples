// This extra example extends algorithms basics with a best-streak scan.
// Example purpose: track the longest rising streak with one pass.

package main

import "fmt"

func longestRisingStreak(values []int) (int, []int) {
	if len(values) == 0 {
		return 0, []int{}
	}

	bestLength := 1
	bestStart := 0
	currentLength := 1
	currentStart := 0

	for index := 1; index < len(values); index++ {
		if values[index] > values[index-1] {
			currentLength++
		} else {
			currentLength = 1
			currentStart = index
		}

		if currentLength > bestLength {
			bestLength = currentLength
			bestStart = currentStart
		}
	}

	streak := append([]int{}, values[bestStart:bestStart+bestLength]...)
	return bestLength, streak
}

func main() {
	temperatures := []int{17, 18, 21, 19, 20, 22, 25, 24}
	length, streak := longestRisingStreak(temperatures)

	fmt.Printf("Longest rising streak length: %d\n", length)
	fmt.Printf("Streak values: %v\n", streak)
}
