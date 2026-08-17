// Module focus: Building objects that start valid and stay valid through guarded updates.
// Why it matters: the example makes it possible to construct objects only in valid states before
// the learner tackles the exercises.

package main

import "fmt"

// Separate helpers keep the main path focused on how to construct objects only in valid states.
type Temperature struct {
	celsius float64
}

func NewTemperature(celsiusValue float64) *Temperature {
	if celsiusValue < -273.15 {
		celsiusValue = -273.15
	}

	return &Temperature{celsius: celsiusValue}
}

func (t *Temperature) SetCelsius(newValue float64) bool {
	if newValue < -273.15 {
		return false
	}

	t.celsius = newValue
	return true
}

func (t *Temperature) Celsius() float64 {
	return t.celsius
}

// Fixed inputs make the consequence of building structs directly and bypassing constructor guards
// visible and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	temperature := NewTemperature(-500.0)
	// The printed result shows whether the program can keep mutations from violating established
	// invariants.
	fmt.Printf("Initial value (clamped): %.2f C\n", temperature.Celsius())

	updated := temperature.SetCelsius(25.0)
	fmt.Printf("Set to 25.0 success: %v\n", updated)
	fmt.Printf("Current value: %.2f C\n", temperature.Celsius())

	rejected := temperature.SetCelsius(-300.0)
	fmt.Printf("Set to -300.0 success: %v\n", rejected)

	fmt.Printf("Current value: %.2f C\n", temperature.Celsius())
}
