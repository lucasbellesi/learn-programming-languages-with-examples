package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Enter row (name,age,city): ")
	row, _ := reader.ReadString('\n')
	row = strings.TrimRight(row, "\r\n")

	firstComma := strings.Index(row, ",")
	if firstComma < 0 {
		fmt.Println("Invalid format. Missing commas.")
		return
	}

	secondComma := strings.Index(row[firstComma+1:], ",")
	if secondComma < 0 {
		fmt.Println("Invalid format. Missing second comma.")
		return
	}
	secondComma += firstComma + 1

	name := row[:firstComma]
	age := row[firstComma+1 : secondComma]
	city := row[secondComma+1:]

	if name == "" || age == "" || city == "" {
		fmt.Println("Invalid format. Empty field detected.")
		return
	}

	fmt.Printf("Name: %s\n", name)
	fmt.Printf("Age: %s\n", age)
	fmt.Printf("City: %s\n", city)
}
