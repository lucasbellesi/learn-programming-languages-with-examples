// This helper example focuses on showing one focused overload or helper so the main example stays easy to scan.

// This extra example extends functions with runtime-type dispatch.

package main

import "fmt"

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
func printValue(value any) {
	switch typed := value.(type) {
	case int:
		fmt.Printf("Integer value: %d\n", typed)
	case float64:
		fmt.Printf("Float value: %.5f\n", typed)
	case string:
		fmt.Printf("String value: %s\n", typed)
	default:
		fmt.Printf("Unsupported value: %v\n", typed)
	}
}

func main() {
	printValue(42)
	printValue(3.14159)
	printValue("Hello from runtime dispatch")
}
