package main

import "fmt"

type Shape interface {
	Area() float64
}

type Triangle struct {
	base   float64
	height float64
}

func (t Triangle) Area() float64 {
	return 0.5 * t.base * t.height
}

func main() {
	var baseValue float64
	var heightValue float64

	fmt.Print("Enter base and height: ")
	if _, err := fmt.Scan(&baseValue, &heightValue); err != nil {
		fmt.Println("Invalid input.")
		return
	}

	if baseValue <= 0 || heightValue <= 0 {
		fmt.Println("Base and height must be positive.")
		return
	}

	triangle := Triangle{base: baseValue, height: heightValue}
	fmt.Printf("Triangle area: %v\n", triangle.Area())
}
