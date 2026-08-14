package main

import "fmt"

type operation func(int, int) (int, bool)

func buildRegistry() map[string]operation {
	return map[string]operation{
		"add": func(left, right int) (int, bool) { return left + right, true },
		"sub": func(left, right int) (int, bool) { return left - right, true },
		"mul": func(left, right int) (int, bool) { return left * right, true },
		"div": func(left, right int) (int, bool) {
			if right == 0 {
				return 0, false
			}
			return left / right, true
		},
	}
}

func main() {
	var command string
	var left, right int
	fmt.Print("Command and operands: ")
	if _, err := fmt.Scan(&command, &left, &right); err != nil {
		fmt.Println("Invalid input.")
		return
	}

	registry := buildRegistry()
	handler, ok := registry[command]
	if !ok {
		fmt.Println("Unsupported command.")
		return
	}

	result, success := handler(left, right)
	if !success {
		fmt.Println("Operation failed.")
		return
	}

	fmt.Printf("Result: %d\n", result)
}
