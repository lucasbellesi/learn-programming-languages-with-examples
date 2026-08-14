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

	total := 0
	for i := 0; i < count; i++ {
		var value int
		fmt.Printf("Value %d: ", i+1)
		fmt.Scanln(&value)
		total += value
	}

	fmt.Printf("Sum: %d\n", total)
	fmt.Printf("Average: %.2f\n", float64(total)/float64(count))
}
