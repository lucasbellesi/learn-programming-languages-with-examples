// This extra example extends control-flow with a menu-driven loop.
// Example purpose: show repeated branching and state updates.

package main

import "fmt"

func main() {
	currentSum := 0

	for {
		fmt.Println("\nMenu")
		fmt.Println("1) Add number to sum")
		fmt.Println("2) Show current sum")
		fmt.Println("3) Reset sum")
		fmt.Println("4) Exit")
		fmt.Print("Choose an option: ")

		var choice int
		if _, err := fmt.Scan(&choice); err != nil {
			fmt.Println("Invalid option. Try again.")
			return
		}

		switch choice {
		case 1:
			var number int
			fmt.Print("Enter a number: ")
			if _, err := fmt.Scan(&number); err != nil {
				fmt.Println("Invalid number. Try again.")
				return
			}
			currentSum += number
			fmt.Printf("Added. New sum is %d.\n", currentSum)
		case 2:
			fmt.Printf("Current sum: %d\n", currentSum)
		case 3:
			currentSum = 0
			fmt.Println("Sum reset to 0.")
		case 4:
			fmt.Println("Goodbye.")
			return
		default:
			fmt.Println("Invalid option. Try again.")
		}
	}
}
