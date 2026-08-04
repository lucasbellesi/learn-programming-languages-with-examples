package main

import "fmt"

func main() {
	var product string
	var price float64
	var quantity int

	fmt.Print("Enter product price quantity: ")
	_, err := fmt.Scanf("%s %f %d", &product, &price, &quantity)
	if err != nil {
		fmt.Println("Invalid format. Use: product price quantity")
		return
	}

	total := price * float64(quantity)
	fmt.Printf("Product: %s\n", product)
	fmt.Printf("Total price: %.2f\n", total)
}
