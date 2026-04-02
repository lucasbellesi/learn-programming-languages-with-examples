// Module focus: Formatting values so output is easier to read and compare.
// Why it matters: practicing formatted output and iomanip patterns makes exercises and checkpoints easier to reason about.

package main

import "fmt"

// Helper setup for formatted output and iomanip; this keeps the walkthrough readable.
type Item struct {
	Name      string
	Quantity  int
	UnitPrice float64
}

// Walk through one fixed scenario so formatted output and iomanip behavior stays repeatable.
func main() {
	// Prepare sample inputs that exercise the key formatted output and iomanip path.
	items := []Item{
		{"Notebook", 2, 3.5},
		{"Pencil", 5, 0.8},
		{"Backpack", 1, 29.99},
	}

	// Report values so learners can verify the formatted output and iomanip outcome.
	fmt.Printf("%-12s%6s%10s%10s\n", "Item", "Qty", "Unit", "Total")
	fmt.Println("--------------------------------------")

	grandTotal := 0.0
	for _, item := range items {
		total := float64(item.Quantity) * item.UnitPrice
		grandTotal += total
		fmt.Printf("%-12s%6d%10.2f%10.2f\n", item.Name, item.Quantity, item.UnitPrice, total)
	}

	fmt.Println("--------------------------------------")
	fmt.Printf("%-28s%10.2f\n", "Grand total", grandTotal)
}
