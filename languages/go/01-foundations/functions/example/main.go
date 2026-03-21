package main

import "fmt"

func add(a int, b int) int {
    return a + b
}

func swapInSlice(values []int, i int, j int) {
    values[i], values[j] = values[j], values[i]
}

func printSlice(values []int) {
    fmt.Println(values)
}

func main() {
    fmt.Println(add(4, 6))

    numbers := []int{10, 20, 30}
    printSlice(numbers)
    swapInSlice(numbers, 0, 1)
    printSlice(numbers)
}
