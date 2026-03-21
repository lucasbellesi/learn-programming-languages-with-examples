package main

import "fmt"

func main() {
    var fullName string
    var age int
    var gpa float64

    fmt.Print("Enter your first name: ")
    fmt.Scanln(&fullName)

    fmt.Print("Enter your age: ")
    fmt.Scanln(&age)

    fmt.Print("Enter your GPA: ")
    fmt.Scanln(&gpa)

    fmt.Println("\n--- Student Summary ---")
    fmt.Printf("Name: %s\n", fullName)
    fmt.Printf("Age: %d\n", age)
    fmt.Printf("GPA: %.2f\n", gpa)
    fmt.Printf("Adult: %t\n", age >= 18)
}
