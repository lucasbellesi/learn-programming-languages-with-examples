// Example purpose: show a modular structure by separating pricing, formatting, and orchestration.

package main

import "fmt"

type lineItem struct {
	name      string
	quantity  int
	unitPrice float64
}

type invoiceSummary struct {
	subtotal      float64
	discountValue float64
	taxValue      float64
	total         float64
}

func buildSummary(items []lineItem, discountPercent, taxPercent float64) invoiceSummary {
	subtotal := 0.0
	for _, item := range items {
		subtotal += float64(item.quantity) * item.unitPrice
	}
	discountValue := subtotal * (discountPercent / 100.0)
	taxedBase := subtotal - discountValue
	taxValue := taxedBase * (taxPercent / 100.0)
	return invoiceSummary{
		subtotal:      subtotal,
		discountValue: discountValue,
		taxValue:      taxValue,
		total:         taxedBase + taxValue,
	}
}

func renderSummary(summary invoiceSummary) string {
	return fmt.Sprintf(
		"Subtotal: %.2f\nDiscount: %.2f\nTax: %.2f\nTotal: %.2f",
		summary.subtotal,
		summary.discountValue,
		summary.taxValue,
		summary.total,
	)
}

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
