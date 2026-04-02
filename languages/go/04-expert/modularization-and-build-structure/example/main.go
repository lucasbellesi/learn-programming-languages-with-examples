// Module focus: Splitting responsibilities so entrypoints and helpers stay focused.
// Why it matters: practicing modularization and build structure patterns makes exercises and checkpoints easier to reason about.

package main

import "fmt"

// Walk through one fixed scenario so modularization and build structure behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key modularization and build structure path.
	items := []lineItem{
		{name: "Notebook", quantity: 2, unitPrice: 3.50},
		{name: "Pencil", quantity: 5, unitPrice: 0.80},
		{name: "Backpack", quantity: 1, unitPrice: 29.99},
	}

	summary := buildSummary(items, 10.0, 7.5)

	// Report values so learners can verify the modularization and build structure outcome.
	fmt.Println(renderSummary(summary))
}
