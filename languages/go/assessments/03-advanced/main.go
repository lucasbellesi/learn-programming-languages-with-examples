package main

import (
	"fmt"
	"math"
)

type Shape interface {
	Area() float64
	Name() string
}

type Circle struct {
	radius float64
}

func (c Circle) Area() float64 {
	return math.Pi * c.radius * c.radius
}

func (c Circle) Name() string {
	return "Circle"
}

type Rectangle struct {
	width  float64
	height float64
}

func (r Rectangle) Area() float64 {
	return r.width * r.height
}

func (r Rectangle) Name() string {
	return "Rectangle"
}

func printSlice[T any](values []T, label string) {
	fmt.Printf("%s: [", label)
	for index, value := range values {
		fmt.Print(value)
		if index+1 < len(values) {
			fmt.Print(", ")
		}
	}
	fmt.Println("]")
}

func main() {
	shapes := []Shape{
		Circle{radius: 2.0},
		Rectangle{width: 3.0, height: 4.0},
		Circle{radius: 1.5},
	}

	areas := make([]float64, 0, len(shapes))

	fmt.Println("Shape areas:")
	for _, shape := range shapes {
		value := shape.Area()
		areas = append(areas, value)
		fmt.Printf("- %s: %v\n", shape.Name(), value)
	}

	totalArea := 0.0
	minArea := areas[0]
	maxArea := areas[0]

	for _, area := range areas {
		totalArea += area
		if area < minArea {
			minArea = area
		}
		if area > maxArea {
			maxArea = area
		}
	}

	fmt.Printf("Total area: %v\n", totalArea)
	fmt.Printf("Minimum area: %v\n", minArea)
	fmt.Printf("Maximum area: %v\n", maxArea)

	printSlice([]int{1, 2, 3, 4}, "Sample counts")
	printSlice(areas, "Computed areas")
}
