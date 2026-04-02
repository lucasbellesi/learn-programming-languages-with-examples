// This example shows formatting values so output is easier to read and compare.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import "fmt"

// Define the reusable pieces first so the main flow can focus on one observable scenario.
type Item struct {
	Name      string
	Quantity  int
	UnitPrice float64
}

// Run one deterministic scenario so the console output makes formatting values so output is easier to read and compare easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	items := []Item{
		{"Notebook", 2, 3.5},
		{"Pencil", 5, 0.8},
		{"Backpack", 1, 29.99},
	}

	// Print the observed state here so learners can connect the code path to a concrete result.
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
