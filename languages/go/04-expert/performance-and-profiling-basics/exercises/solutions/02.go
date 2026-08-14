package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Element count: ")
	line, _ := reader.ReadString('\n')
	count, err := strconv.Atoi(strings.TrimSpace(line))
	if err != nil {
		fmt.Println("Invalid element count.")
		return
	}
	if count < 0 {
		fmt.Println("Element count cannot be negative.")
		return
	}

	noCapacity := measure(func() { _ = fillWithoutCapacity(count) })
	withCapacity := measure(func() { _ = fillWithCapacity(count) })
	fmt.Printf("Without capacity: %v\n", noCapacity)
	fmt.Printf("With capacity: %v\n", withCapacity)
}

func measure(action func()) time.Duration {
	start := time.Now()
	action()
	return time.Since(start)
}

func fillWithoutCapacity(count int) []int {
	values := []int{}
	for index := 0; index < count; index++ {
		values = append(values, index)
	}
	return values
}

func fillWithCapacity(count int) []int {
	values := make([]int, 0, count)
	for index := 0; index < count; index++ {
		values = append(values, index)
	}
	return values
}
