package main

import "fmt"

func main() {
	var count int
	fmt.Print("How many integers? ")
	fmt.Scanln(&count)

	if count <= 0 {
		fmt.Println("Please enter a positive count.")
		return
	}

	values := make([]int, 0, count)
	for i := 0; i < count; i++ {
		var value int
		fmt.Scanln(&value)
		values = append(values, value)
	}

	var target int
	fmt.Print("Target value: ")
	fmt.Scanln(&target)

	frequency := 0
	for _, value := range values {
		if value == target {
			frequency++
		}
	}

	fmt.Printf("Frequency of %d: %d\n", target, frequency)
}
