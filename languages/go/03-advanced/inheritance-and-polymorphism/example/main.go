// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import (
	"fmt"
	"math"
)

type Shape interface {
	Area() float64
	Name() string
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

type Circle struct {
	radius float64
}

func (c Circle) Area() float64 {
	return math.Pi * c.radius * c.radius
}

func (c Circle) Name() string {
	return "Circle"
}

func main() {
	// Program flow: create mixed shapes and evaluate them through one interface.
	shapes := []Shape{
		Rectangle{width: 3.0, height: 4.0},
		Circle{radius: 2.0},
	}

	// Intent: polymorphic iteration keeps logic independent from concrete structs.
	for _, shape := range shapes {
		fmt.Printf("%s area: %.2f\n", shape.Name(), shape.Area())
	}
}
