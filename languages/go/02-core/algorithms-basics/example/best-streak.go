// This helper example focuses on isolating one pass over the data so the main example can explain the result clearly.

// This extra example extends algorithms basics with a best-streak scan.

package main

import "fmt"

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
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
