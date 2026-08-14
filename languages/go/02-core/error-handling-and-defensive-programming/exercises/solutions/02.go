package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	for {
		fmt.Print("Enter two numbers to divide (a b): ")
		line, _ := reader.ReadString('\n')
		parts := strings.Fields(line)

		if len(parts) != 2 {
			fmt.Println("Invalid input type. Try again.")
			continue
		}

		a, errA := strconv.ParseFloat(parts[0], 64)
		b, errB := strconv.ParseFloat(parts[1], 64)
		if errA != nil || errB != nil {
			fmt.Println("Invalid input type. Try again.")
			continue
		}

		if b == 0.0 {
			fmt.Println("Divisor cannot be zero. Try again.")
			continue
		}

		fmt.Printf("Result: %v\n", a/b)
		break
	}
}
