// Module focus: Building objects that start valid and stay valid through guarded updates.
// Why it matters: practicing constructors and invariants patterns makes exercises and checkpoints easier to reason about.

package main

import "fmt"

// Helper setup for constructors and invariants; this keeps the walkthrough readable.
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

// Walk through one fixed scenario so constructors and invariants behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key constructors and invariants path.
	temperature := NewTemperature(-500.0)
	// Report values so learners can verify the constructors and invariants outcome.
	fmt.Printf("Initial value (clamped): %.2f C\n", temperature.Celsius())

	updated := temperature.SetCelsius(25.0)
	fmt.Printf("Set to 25.0 success: %v\n", updated)
	fmt.Printf("Current value: %.2f C\n", temperature.Celsius())

	rejected := temperature.SetCelsius(-300.0)
	fmt.Printf("Set to -300.0 success: %v\n", rejected)

	fmt.Printf("Current value: %.2f C\n", temperature.Celsius())
}
