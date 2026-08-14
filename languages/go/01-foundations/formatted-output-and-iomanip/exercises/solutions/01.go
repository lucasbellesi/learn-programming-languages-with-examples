package main

import "fmt"

type Product struct {
	Name     string
	Price    float64
	Quantity int
}

func main() {
	var count int
	fmt.Print("How many products? ")
	fmt.Scanln(&count)

	if count <= 0 {
		fmt.Println("Please enter a positive count.")
		return
	}

	products := make([]Product, 0, count)
	for i := 0; i < count; i++ {
		var product Product
		fmt.Printf("Product %d name: ", i+1)
		fmt.Scanln(&product.Name)
		fmt.Printf("Product %d price: ", i+1)
		fmt.Scanln(&product.Price)
		fmt.Printf("Product %d quantity: ", i+1)
		fmt.Scanln(&product.Quantity)
		products = append(products, product)
	}

	fmt.Printf("%-16s%10s%8s%12s\n", "Product", "Price", "Qty", "Total")
	fmt.Println("----------------------------------------------")

	grandTotal := 0.0
	for _, product := range products {
		total := product.Price * float64(product.Quantity)
		grandTotal += total
		fmt.Printf("%-16s%10.2f%8d%12.2f\n", product.Name, product.Price, product.Quantity, total)
	}

	fmt.Println("----------------------------------------------")
	fmt.Printf("%-34s%12.2f\n", "Grand total", grandTotal)
}
