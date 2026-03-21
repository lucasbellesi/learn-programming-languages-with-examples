package main

import "fmt"

type Item struct {
	Name      string
	Quantity  int
	UnitPrice float64
}

func main() {
	items := []Item{
		{"Notebook", 2, 3.5},
		{"Pencil", 5, 0.8},
		{"Backpack", 1, 29.99},
	}

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
