// Module focus: Splitting responsibilities so entrypoints and helpers stay focused.
// Why it matters: the example makes it possible to separate public contracts from implementation
// details before the learner tackles the exercises.

package main

import "fmt"

// Fixed inputs make the consequence of putting every concern directly into `main` visible and
// repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
	items := []lineItem{
		{name: "Notebook", quantity: 2, unitPrice: 3.50},
		{name: "Pencil", quantity: 5, unitPrice: 0.80},
		{name: "Backpack", quantity: 1, unitPrice: 29.99},
	}

	summary := buildSummary(items, 10.0, 7.5)

	// The printed result shows whether the program can organize a multi-file program with an
	// explicit build boundary.
	fmt.Println(renderSummary(summary))
}
