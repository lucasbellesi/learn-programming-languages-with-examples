// This extra example extends arrays-and-vectors with a focused filtering task.
// Example purpose: isolate slice building and threshold-based filtering.

package main

import "fmt"

func main() {
	var count int
	fmt.Print("How many numbers? ")
	if _, err := fmt.Scan(&count); err != nil || count <= 0 {
		fmt.Println("Please enter a positive count.")
		return
	}

	values := make([]int, 0, count)
	for index := 0; index < count; index++ {
		var value int
		fmt.Printf("Value %d: ", index+1)
		if _, err := fmt.Scan(&value); err != nil {
			fmt.Println("Please enter valid integers only.")
			return
		}
		values = append(values, value)
	}

	var threshold int
	fmt.Print("Filter values greater than or equal to: ")
	if _, err := fmt.Scan(&threshold); err != nil {
		fmt.Println("Please enter a valid threshold.")
		return
	}

	fmt.Print("Filtered values: ")
	printedAny := false
	for _, value := range values {
		if value >= threshold {
			if printedAny {
				fmt.Print(", ")
			}
			fmt.Print(value)
			printedAny = true
		}
	}

	if !printedAny {
		fmt.Print("none")
	}
	fmt.Println()
}
