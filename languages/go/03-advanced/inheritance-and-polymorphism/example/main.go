// This example shows treating different concrete types through one common interface.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import (
	"fmt"
	"math"
)

// Define the reusable pieces first so the main flow can focus on one observable scenario.
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

// Run one deterministic scenario so the console output makes treating different concrete types through one common interface easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	shapes := []Shape{
		Rectangle{width: 3.0, height: 4.0},
		Circle{radius: 2.0},
	}

	for _, shape := range shapes {
		// Print the observed state here so learners can connect the code path to a concrete result.
		fmt.Printf("%s area: %.2f\n", shape.Name(), shape.Area())
	}
}
