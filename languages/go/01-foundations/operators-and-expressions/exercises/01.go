package main

import "fmt"

func main() {
	var totalSeconds int
	fmt.Print("Enter total seconds: ")
	fmt.Scanln(&totalSeconds)

	if totalSeconds < 0 {
		fmt.Println("Please enter a non-negative value.")
		return
	}

	hours := totalSeconds / 3600
	minutes := (totalSeconds % 3600) / 60
	seconds := totalSeconds % 60

	fmt.Printf("Hours: %d\n", hours)
	fmt.Printf("Minutes: %d\n", minutes)
	fmt.Printf("Seconds: %d\n", seconds)
}
