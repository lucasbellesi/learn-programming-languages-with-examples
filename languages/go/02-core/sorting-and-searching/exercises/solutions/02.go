package main

import "fmt"

func main() {
	var n int
	fmt.Print("How many sorted values? ")
	fmt.Scanln(&n)

	if n <= 0 {
		fmt.Println("Please enter a positive count.")
		return
	}

	values := make([]int, 0, n)
	for i := 0; i < n; i++ {
		var value int
		fmt.Scanln(&value)
		values = append(values, value)
	}

	var target int
	fmt.Print("Target: ")
	fmt.Scanln(&target)

	left := 0
	right := n - 1
	index := -1

	for left <= right {
		mid := left + (right-left)/2
		midValue := values[mid]

		if midValue == target {
			index = mid
			break
		}

		if midValue < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	fmt.Printf("Index: %d\n", index)
}
