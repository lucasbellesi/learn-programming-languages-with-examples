// Module focus: Treating different concrete types through one common interface.
// Why it matters: the example makes it possible to program against a shared behavioral
// abstraction before the learner tackles the exercises.

package main

import (
	"fmt"
	"math"
)

// Separate helpers keep the main path focused on how to program against a shared behavioral
// abstraction.
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

// Fixed inputs make the consequence of expecting inheritance syntax instead of
// composition/interfaces visible and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	shapes := []Shape{
		Rectangle{width: 3.0, height: 4.0},
		Circle{radius: 2.0},
	}

	for _, shape := range shapes {
		// The printed result shows whether the program can use dynamic dispatch without unsafe type
		// assumptions.
		fmt.Printf("%s area: %.2f\n", shape.Name(), shape.Area())
	}
}
