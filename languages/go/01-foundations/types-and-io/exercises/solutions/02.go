package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Print("Enter product price quantity: ")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	parts := strings.Fields(scanner.Text())
	if scanner.Err() != nil || len(parts) != 3 {
		fmt.Println("Invalid format. Use: product price quantity")
		return
	}

	product := parts[0]
	price, priceErr := strconv.ParseFloat(parts[1], 64)
	quantity, quantityErr := strconv.Atoi(parts[2])
	if priceErr != nil || quantityErr != nil {
		fmt.Println("Invalid format. Use: product price quantity")
		return
	}

	total := price * float64(quantity)
	fmt.Printf("Product: %s\n", product)
	fmt.Printf("Total price: %.2f\n", total)
}
