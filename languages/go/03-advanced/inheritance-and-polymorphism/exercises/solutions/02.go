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
	var count int
	if _, err := fmt.Scan(&count); err != nil || count < 0 {
		fmt.Println("Expected a non-negative shape count.")
		return
	}

	shapes := make([]Shape, 0, count)
	for index := 0; index < count; index++ {
		var kind string
		if _, err := fmt.Scan(&kind); err != nil {
			fmt.Println("Missing shape data.")
			return
		}
		switch kind {
		case "rectangle":
			var width float64
			var height float64
			if _, err := fmt.Scan(&width, &height); err != nil {
				fmt.Println("Invalid rectangle.")
				return
			}
			shapes = append(shapes, Rectangle{width: width, height: height})
		case "circle":
			var radius float64
			if _, err := fmt.Scan(&radius); err != nil {
				fmt.Println("Invalid circle.")
				return
			}
			shapes = append(shapes, Circle{radius: radius})
		default:
			fmt.Println("Unknown shape type.")
			return
		}
	}

	totalArea := 0.0
	for _, shape := range shapes {
		totalArea += shape.Area()
	}

	fmt.Printf("Total area: %v\n", totalArea)
}
