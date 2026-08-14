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
	fmt.Print("Items to produce: ")
	line, _ := reader.ReadString('\n')
	count, err := strconv.Atoi(strings.TrimSpace(line))
	if err != nil {
		fmt.Println("Invalid item count.")
		return
	}
	if count < 0 {
		fmt.Println("Item count cannot be negative.")
		return
	}

	queue := make(chan int)
	done := make(chan int, 1)

	go func() {
		consumed := 0
		for value := range queue {
			fmt.Printf("Consumed %d\n", value)
			consumed++
		}
		done <- consumed
	}()

	for value := 1; value <= count; value++ {
		fmt.Printf("Produced %d\n", value)
		queue <- value
	}
	close(queue)

	fmt.Printf("Produced total: %d\n", count)
	fmt.Printf("Consumed total: %d\n", <-done)
}
