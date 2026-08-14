package main

import "fmt"

func main() {
	var subtotal, discountPercent, taxPercent float64

	fmt.Print("Subtotal: ")
	fmt.Scanln(&subtotal)
	fmt.Print("Discount percent: ")
	fmt.Scanln(&discountPercent)
	fmt.Print("Tax percent: ")
	fmt.Scanln(&taxPercent)

	if subtotal < 0 {
		fmt.Println("Subtotal must be non-negative.")
		return
	}

	discountValue := subtotal * (discountPercent / 100)
	discountedTotal := subtotal - discountValue
	taxValue := discountedTotal * (taxPercent / 100)
	finalTotal := discountedTotal + taxValue

	fmt.Printf("Discount value: %.2f\n", discountValue)
	fmt.Printf("Tax value: %.2f\n", taxValue)
	fmt.Printf("Final total: %.2f\n", finalTotal)
}
