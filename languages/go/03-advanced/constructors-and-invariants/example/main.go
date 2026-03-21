// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import "fmt"

type Temperature struct {
	celsius float64
}

func NewTemperature(celsiusValue float64) *Temperature {
	// Intent: enforce the invariant at construction time.
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

func main() {
	// Program flow: construct with invalid input, then apply valid and invalid updates.
	temperature := NewTemperature(-500.0)
	fmt.Printf("Initial value (clamped): %.2f C\n", temperature.Celsius())

	updated := temperature.SetCelsius(25.0)
	fmt.Printf("Set to 25.0 success: %v\n", updated)
	fmt.Printf("Current value: %.2f C\n", temperature.Celsius())

	rejected := temperature.SetCelsius(-300.0)
	fmt.Printf("Set to -300.0 success: %v\n", rejected)

	// Intent: final state confirms that invariant was preserved.
	fmt.Printf("Current value: %.2f C\n", temperature.Celsius())
}
