package main

import "fmt"

func main() {
	var n int
	fmt.Print("How many integers? ")
	fmt.Scanln(&n)

	if n <= 0 {
		fmt.Println("Please enter a positive count.")
		return
	}

	values := make([]int, 0, n)
	for i := 0; i < n; i++ {
		var value int
		fmt.Printf("Value %d: ", i+1)
		fmt.Scanln(&value)
		values = append(values, value)
	}

	minValue := values[0]
	maxValue := values[0]
	evenCount := 0

	for _, value := range values {
		if value < minValue {
			minValue = value
		}
		if value > maxValue {
			maxValue = value
		}
		if value%2 == 0 {
			evenCount++
		}
	}

	fmt.Printf("Minimum: %d\n", minValue)
	fmt.Printf("Maximum: %d\n", maxValue)
	fmt.Printf("Even numbers: %d\n", evenCount)
}
