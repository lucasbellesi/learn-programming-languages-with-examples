package main

import "fmt"

type Rectangle struct {
	Width  float64
	Height float64
}

func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

func (r Rectangle) Perimeter() float64 {
	return 2.0 * (r.Width + r.Height)
}

func main() {
	var width float64
	var height float64

	fmt.Print("Enter width and height: ")
	if _, err := fmt.Scan(&width, &height); err != nil {
		fmt.Println("Invalid input. Enter exactly two numbers.")
		return
	}

	if width <= 0 || height <= 0 {
		fmt.Println("Width and height must be positive.")
		return
	}

	rectangle := Rectangle{Width: width, Height: height}
	fmt.Printf("Area: %v\n", rectangle.Area())
	fmt.Printf("Perimeter: %v\n", rectangle.Perimeter())
}
