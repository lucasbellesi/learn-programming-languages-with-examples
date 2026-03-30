package main

import "fmt"

func validatePercent(value float64) bool {
	return value >= 0.0 && value <= 100.0
}

func buildTotals(subtotal, discountPercent, taxPercent float64) (float64, float64, float64, bool) {
	if subtotal < 0.0 || !validatePercent(discountPercent) || !validatePercent(taxPercent) {
		return 0.0, 0.0, 0.0, false
	}

	discountValue := subtotal * (discountPercent / 100.0)
	taxedBase := subtotal - discountValue
	taxValue := taxedBase * (taxPercent / 100.0)
	return discountValue, taxValue, taxedBase + taxValue, true
}

func main() {
	var subtotal, discountPercent, taxPercent float64
	fmt.Print("Subtotal, discount %, tax %: ")
	if _, err := fmt.Scan(&subtotal, &discountPercent, &taxPercent); err != nil {
		fmt.Println("Invalid input.")
		return
	}

	discountValue, taxValue, total, ok := buildTotals(subtotal, discountPercent, taxPercent)
	if !ok {
		fmt.Println("Values out of range.")
		return
	}

	fmt.Printf("Discount: %.2f\n", discountValue)
	fmt.Printf("Tax: %.2f\n", taxValue)
	fmt.Printf("Total: %.2f\n", total)
}
