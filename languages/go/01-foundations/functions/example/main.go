// This example demonstrates functions concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import "fmt"

func add(a int, b int) int {
    return a + b
}

func swapInSlice(values []int, i int, j int) {
    values[i], values[j] = values[j], values[i]
}

func printSlice(values []int) {
    // Intent: print intermediate or final output for quick behavior verification.
    fmt.Println(values)
}

func main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    fmt.Println(add(4, 6))

    numbers := []int{10, 20, 30}
    printSlice(numbers)
    swapInSlice(numbers, 0, 1)
    printSlice(numbers)
}
