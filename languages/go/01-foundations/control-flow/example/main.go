package main

import "fmt"

func main() {
    var value int
    fmt.Print("Enter an integer: ")
    fmt.Scanln(&value)

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
    for i := 1; i <= n; i++ {
        factorial *= i
    }

    fmt.Printf("factorial(%d) = %d\n", n, factorial)
    fmt.Println("Numbers 1..N:")
    for i := 1; i <= n; i++ {
        fmt.Println(i)
    }
}
