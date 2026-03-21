package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter text: ")
	line, _ := reader.ReadString('\n')

	words := strings.Fields(line)
	fmt.Printf("Word count: %d\n", len(words))
}
