// Example purpose: show a modular structure by separating pricing, formatting, and orchestration.

package main

import "fmt"

func main() {
	// Program flow: define input data, delegate calculations, then format a report.
	items := []lineItem{
		{name: "Notebook", quantity: 2, unitPrice: 3.50},
		{name: "Pencil", quantity: 5, unitPrice: 0.80},
		{name: "Backpack", quantity: 1, unitPrice: 29.99},
	}

	summary := buildSummary(items, 10.0, 7.5)

	// Intent: keep console output in main while reusable logic stays in helpers.
	fmt.Println(renderSummary(summary))
}
