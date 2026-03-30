package main

import "fmt"

func renderSummary(summary invoiceSummary) string {
	return fmt.Sprintf(
		"Subtotal: %.2f\nDiscount: %.2f\nTax: %.2f\nTotal: %.2f",
		summary.subtotal,
		summary.discountValue,
		summary.taxValue,
		summary.total,
	)
}
