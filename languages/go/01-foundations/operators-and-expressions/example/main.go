package main

import "fmt"

func main() {
	var totalSeconds int
	fmt.Print("Enter total seconds: ")
	fmt.Scanln(&totalSeconds)

	hours := totalSeconds / 3600
	minutes := (totalSeconds % 3600) / 60
	seconds := totalSeconds % 60

	fmt.Printf("Time: %d:%02d:%02d\n", hours, minutes, seconds)

	var a, b float64
	fmt.Print("Enter first number: ")
	fmt.Scanln(&a)
	fmt.Print("Enter second number: ")
	fmt.Scanln(&b)

	fmt.Printf("Sum: %.4f\n", a+b)
	fmt.Printf("Difference: %.4f\n", a-b)
	fmt.Printf("Product: %.4f\n", a*b)

	if b != 0 {
		fmt.Printf("Division: %.4f\n", a/b)
	} else {
		fmt.Println("Division is not possible because second number is zero.")
	}
}
