// This example shows building objects that start valid and stay valid through guarded updates.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import "fmt"

// Define the reusable pieces first so the main flow can focus on one observable scenario.
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

// Run one deterministic scenario so the console output makes building objects that start valid and stay valid through guarded updates easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	temperature := NewTemperature(-500.0)
	// Print the observed state here so learners can connect the code path to a concrete result.
	fmt.Printf("Initial value (clamped): %.2f C\n", temperature.Celsius())

	updated := temperature.SetCelsius(25.0)
	fmt.Printf("Set to 25.0 success: %v\n", updated)
	fmt.Printf("Current value: %.2f C\n", temperature.Celsius())

	rejected := temperature.SetCelsius(-300.0)
	fmt.Printf("Set to -300.0 success: %v\n", rejected)

	fmt.Printf("Current value: %.2f C\n", temperature.Celsius())
}
