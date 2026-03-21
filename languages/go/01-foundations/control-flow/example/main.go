// This example demonstrates control flow concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

package main

import "fmt"

func main() {
    // Program flow: collect input, apply core logic, then print a verifiable result.
    var value int
    // Intent: print intermediate or final output for quick behavior verification.
    fmt.Print("Enter an integer: ")
    // Intent: gather typed input first so later operations are predictable.
    fmt.Scanln(&value)

    // Intent: guard invalid or edge-case paths before the main path continues.
    if value > 0 {
        fmt.Println("positive")
    } else if value < 0 {
        fmt.Println("negative")
    } else {
        fmt.Println("zero")
    }

    var n int
    fmt.Print("Enter N: ")
    fmt.Scanln(&n)

    if n < 0 {
        fmt.Println("N must be non-negative.")
        return
    }

    factorial := 1
    // Intent: iterate through data in a clear and deterministic order.
    for i := 1; i <= n; i++ {
        factorial *= i
    }

    fmt.Printf("factorial(%d) = %d\n", n, factorial)
    fmt.Println("Numbers 1..N:")
    for i := 1; i <= n; i++ {
        fmt.Println(i)
    }
}
