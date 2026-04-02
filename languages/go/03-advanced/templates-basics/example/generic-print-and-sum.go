// This helper example focuses on isolating the reusable generic behavior before the example wires it together.

// This extra example extends templates-basics with reusable typed helpers.

package main

import "fmt"

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
type number interface {
	~int | ~float64
}

func printSlice[T any](values []T, label string) {
	fmt.Printf("%s: [", label)
	for index, value := range values {
		if index > 0 {
			fmt.Print(", ")
		}
		fmt.Print(value)
	}
	fmt.Println("]")
}

func sumSlice[T number](values []T) T {
	var total T
	for _, value := range values {
		total += value
	}
	return total
}

func main() {
	numbers := []int{2, 4, 6, 8}
	prices := []float64{1.5, 2.25, 3.75}

	printSlice(numbers, "Numbers")
	printSlice(prices, "Prices")

	fmt.Printf("Sum of numbers: %d\n", sumSlice(numbers))
	fmt.Printf("Sum of prices: %.2f\n", sumSlice(prices))
}
