package main

import "fmt"

func main() {
	var n int
	fmt.Print("How many numbers? ")
	fmt.Scanln(&n)

	if n <= 0 {
		fmt.Println("Please enter a positive count.")
		return
	}

	sum := 0.0
	var value float64

	fmt.Print("Value 1: ")
	fmt.Scanln(&value)
	sum += value
	minValue := value
	maxValue := value

	for i := 2; i <= n; i++ {
		fmt.Printf("Value %d: ", i)
		fmt.Scanln(&value)
		sum += value
		if value < minValue {
			minValue = value
		}
		if value > maxValue {
			maxValue = value
		}
	}

	fmt.Printf("Sum: %.4f\n", sum)
	fmt.Printf("Average: %.4f\n", sum/float64(n))
	fmt.Printf("Minimum: %.4f\n", minValue)
	fmt.Printf("Maximum: %.4f\n", maxValue)
}
