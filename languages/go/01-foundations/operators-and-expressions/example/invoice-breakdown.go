// This extra example extends operators and expressions with an invoice breakdown.
// Example purpose: combine arithmetic operations in a realistic pricing flow.

package main

import "fmt"

func main() {
	subtotal := 84.50
	discountPercent := 12.0
	taxPercent := 21.0
	shipping := 7.50

	discountValue := subtotal * discountPercent / 100.0
	taxableBase := subtotal - discountValue
	taxValue := taxableBase * taxPercent / 100.0
	finalTotal := taxableBase + taxValue + shipping

	fmt.Printf("Subtotal: %.2f\n", subtotal)
	fmt.Printf("Discount: -%.2f\n", discountValue)
	fmt.Printf("Taxable base: %.2f\n", taxableBase)
	fmt.Printf("Tax: +%.2f\n", taxValue)
	fmt.Printf("Shipping: +%.2f\n", shipping)
	fmt.Printf("Final total: %.2f\n", finalTotal)
}
