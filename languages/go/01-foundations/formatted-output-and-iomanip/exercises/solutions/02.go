package main

import "fmt"

func main() {
	var count int
	fmt.Print("How many values? ")
	fmt.Scanln(&count)

	if count <= 0 {
		fmt.Println("Please enter a positive count.")
		return
	}

	values := make([]float64, 0, count)
	for i := 0; i < count; i++ {
		var value float64
		fmt.Scanln(&value)
		values = append(values, value)
	}

	var precision int
	fmt.Print("Decimal precision (0-6): ")
	fmt.Scanln(&precision)

	if precision < 0 || precision > 6 {
		fmt.Println("Precision must be between 0 and 6.")
		return
	}

	sum := 0.0
	minValue := values[0]
	maxValue := values[0]

	for _, value := range values {
		sum += value
		if value < minValue {
			minValue = value
		}
		if value > maxValue {
			maxValue = value
		}
	}

	average := sum / float64(len(values))

	fmt.Printf("Count: %d\n", len(values))
	fmt.Printf("Sum: %.*f\n", precision, sum)
	fmt.Printf("Average: %.*f\n", precision, average)
	fmt.Printf("Minimum: %.*f\n", precision, minValue)
	fmt.Printf("Maximum: %.*f\n", precision, maxValue)
}
