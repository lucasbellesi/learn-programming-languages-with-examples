// Module focus: Treating different concrete types through one common interface.
// Why it matters: practicing inheritance and polymorphism patterns makes exercises and checkpoints easier to reason about.

package main

import (
	"fmt"
	"math"
)

// Helper setup for inheritance and polymorphism; this keeps the walkthrough readable.
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

// Walk through one fixed scenario so inheritance and polymorphism behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key inheritance and polymorphism path.
	shapes := []Shape{
		Rectangle{width: 3.0, height: 4.0},
		Circle{radius: 2.0},
	}

	for _, shape := range shapes {
		// Report values so learners can verify the inheritance and polymorphism outcome.
		fmt.Printf("%s area: %.2f\n", shape.Name(), shape.Area())
	}
}
