package main

import "fmt"

func maxOfThree(a int, b int, c int) int {
    maxValue := a
    if b > maxValue {
        maxValue = b
    }
    if c > maxValue {
        maxValue = c
    }
    return maxValue
}

func main() {
    var x, y, z int
    fmt.Print("Enter three integers: ")
    fmt.Scanln(&x, &y, &z)

    fmt.Printf("Maximum: %d\n", maxOfThree(x, y, z))
}
