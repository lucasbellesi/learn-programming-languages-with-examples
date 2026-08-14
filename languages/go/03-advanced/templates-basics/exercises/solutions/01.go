package main

import "fmt"

func SwapValues[T any](left *T, right *T) {
	temp := *left
	*left = *right
	*right = temp
}

func main() {
	var left int
	var right int

	fmt.Print("Enter two integers: ")
	if _, err := fmt.Scan(&left, &right); err != nil {
		fmt.Println("Invalid input.")
		return
	}

	fmt.Printf("Before swap: %d %d\n", left, right)
	SwapValues(&left, &right)
	fmt.Printf("After swap: %d %d\n", left, right)
}
