package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Counter struct {
	value int
}

func (c *Counter) Increment() {
	c.value++
}

func (c *Counter) Decrement() {
	c.value--
}

func (c *Counter) Reset() {
	c.value = 0
}

func (c *Counter) Value() int {
	return c.value
}

func main() {
	counter := Counter{}
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Println("Commands: inc, dec, reset, stop")
	for {
		fmt.Print("Enter command: ")
		if !scanner.Scan() {
			break
		}

		command := strings.TrimSpace(strings.ToLower(scanner.Text()))

		switch command {
		case "inc":
			counter.Increment()
			fmt.Printf("Current value: %d\n", counter.Value())
		case "dec":
			counter.Decrement()
			fmt.Printf("Current value: %d\n", counter.Value())
		case "reset":
			counter.Reset()
			fmt.Printf("Current value: %d\n", counter.Value())
		case "stop":
			fmt.Printf("Final value: %d\n", counter.Value())
			return
		default:
			fmt.Println("Unknown command.")
		}
	}

	fmt.Printf("Final value: %d\n", counter.Value())
}
