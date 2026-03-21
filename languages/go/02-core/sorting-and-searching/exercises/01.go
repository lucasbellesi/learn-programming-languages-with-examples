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

	values := make([]int, 0, n)
	for i := 0; i < n; i++ {
		var value int
		fmt.Scanln(&value)
		values = append(values, value)
	}

	for i := 0; i < n-1; i++ {
		minIndex := i
		for j := i + 1; j < n; j++ {
			if values[j] < values[minIndex] {
				minIndex = j
			}
		}

		values[i], values[minIndex] = values[minIndex], values[i]
	}

	for _, value := range values {
		fmt.Printf("%d ", value)
	}
	fmt.Println()
}
