package main

import "fmt"

func main() {
    fmt.Println("Enter integers (-1 to stop):")

    sum := 0
    count := 0

    for {
        var value int
        fmt.Scanln(&value)
        if value == -1 {
            break
        }
        sum += value
        count++
    }

    if count == 0 {
        fmt.Println("No values entered.")
        return
    }

    fmt.Printf("Average: %.4f\n", float64(sum)/float64(count))
}
