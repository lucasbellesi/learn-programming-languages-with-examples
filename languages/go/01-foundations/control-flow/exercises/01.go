package main

import "fmt"

func main() {
    var n int
    fmt.Print("Run FizzBuzz up to: ")
    fmt.Scanln(&n)

    if n <= 0 {
        fmt.Println("Please enter a positive N.")
        return
    }

    for i := 1; i <= n; i++ {
        if i%15 == 0 {
            fmt.Println("FizzBuzz")
        } else if i%3 == 0 {
            fmt.Println("Fizz")
        } else if i%5 == 0 {
            fmt.Println("Buzz")
        } else {
            fmt.Println(i)
        }
    }
}
