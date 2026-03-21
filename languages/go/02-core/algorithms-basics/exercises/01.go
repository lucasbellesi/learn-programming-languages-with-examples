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

	var target int
	fmt.Print("Target to find: ")
	fmt.Scanln(&target)

	firstIndex := -1
	for index, value := range values {
		if value == target {
			firstIndex = index
			break
		}
	}

	fmt.Printf("First index: %d\n", firstIndex)
}
