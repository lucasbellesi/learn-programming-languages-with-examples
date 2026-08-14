package main

import "fmt"

type Number interface {
	~int | ~int32 | ~int64 | ~float32 | ~float64
}

func AverageOf[T Number](values []T) float64 {
	if len(values) == 0 {
		return 0.0
	}

	sum := 0.0
	for _, value := range values {
		sum += float64(value)
	}

	return sum / float64(len(values))
}

func main() {
	var count int

	fmt.Print("How many numbers? ")
	if _, err := fmt.Scan(&count); err != nil || count < 0 {
		fmt.Println("Please enter zero or a positive count.")
		return
	}

	values := make([]float64, 0, count)
	for index := 0; index < count; index++ {
		var value float64
		if _, err := fmt.Scan(&value); err != nil {
			fmt.Println("Invalid number.")
			return
		}
		values = append(values, value)
	}

	fmt.Printf("Average: %v\n", AverageOf(values))
}
