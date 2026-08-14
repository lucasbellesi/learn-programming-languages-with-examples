package main

import (
	"fmt"
	"math"
)

type Shape interface {
	Area() float64
}

type Rectangle struct {
	width  float64
	height float64
}

func (r Rectangle) Area() float64 {
	return r.width * r.height
}

type Circle struct {
	radius float64
}

func (c Circle) Area() float64 {
	return math.Pi * c.radius * c.radius
}

func main() {
	shapes := []Shape{
		Rectangle{width: 2.0, height: 5.0},
		Circle{radius: 1.5},
	}

	totalArea := 0.0
	for _, shape := range shapes {
		totalArea += shape.Area()
	}

	fmt.Printf("Total area: %v\n", totalArea)
}
