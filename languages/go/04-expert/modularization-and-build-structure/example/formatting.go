// This helper example focuses on keeping presentation rules separate from calculations and program startup.

package main

import "fmt"

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
func renderSummary(summary invoiceSummary) string {
	return fmt.Sprintf(
		"Subtotal: %.2f\nDiscount: %.2f\nTax: %.2f\nTotal: %.2f",
		summary.subtotal,
		summary.discountValue,
		summary.taxValue,
		summary.total,
	)
}
