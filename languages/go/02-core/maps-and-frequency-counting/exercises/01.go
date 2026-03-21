package main

import "fmt"

func main() {
	var n int
	fmt.Print("How many digits? ")
	fmt.Scanln(&n)

	if n <= 0 {
		fmt.Println("Please enter a positive count.")
		return
	}

	frequency := make(map[int]int)
	for digit := 0; digit <= 9; digit++ {
		frequency[digit] = 0
	}

	for i := 0; i < n; i++ {
		var value int
		fmt.Scanln(&value)
		if value >= 0 && value <= 9 {
			frequency[value]++
		}
	}

	for digit := 0; digit <= 9; digit++ {
		fmt.Printf("%d -> %d\n", digit, frequency[digit])
	}
}
