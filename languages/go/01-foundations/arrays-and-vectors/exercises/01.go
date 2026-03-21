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

	values := make([]int, 0, count)
	for i := 0; i < count; i++ {
		var value int
		fmt.Printf("Value %d: ", i+1)
		fmt.Scanln(&value)
		values = append(values, value)
	}

	fmt.Println("Values in reverse order:")
	for i := len(values) - 1; i >= 0; i-- {
		fmt.Println(values[i])
	}
}
