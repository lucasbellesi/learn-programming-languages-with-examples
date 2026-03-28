// This extra example extends functions with runtime-type dispatch.
// Example purpose: mirror overload-style behavior in a language without function overloading.

package main

import "fmt"

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
