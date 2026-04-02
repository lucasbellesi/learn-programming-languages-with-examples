// This example shows splitting responsibilities so entrypoints and helpers stay focused.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import "fmt"

// Run one deterministic scenario so the console output makes splitting responsibilities so entrypoints and helpers stay focused easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	items := []lineItem{
		{name: "Notebook", quantity: 2, unitPrice: 3.50},
		{name: "Pencil", quantity: 5, unitPrice: 0.80},
		{name: "Backpack", quantity: 1, unitPrice: 29.99},
	}

	summary := buildSummary(items, 10.0, 7.5)

	// Print the observed state here so learners can connect the code path to a concrete result.
	fmt.Println(renderSummary(summary))
}
