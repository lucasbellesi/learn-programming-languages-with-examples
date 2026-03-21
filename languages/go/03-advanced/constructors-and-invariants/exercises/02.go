package main

import "fmt"

type SimpleDate struct {
	month int
	day   int
}

func NewSimpleDate(month int, day int) *SimpleDate {
	return &SimpleDate{month: month, day: day}
}

func (d *SimpleDate) IsValid() bool {
	if d.month < 1 || d.month > 12 {
		return false
	}

	daysInMonth := [12]int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	return d.day >= 1 && d.day <= daysInMonth[d.month-1]
}

func main() {
	var month int
	var day int

	fmt.Print("Enter month and day: ")
	if _, err := fmt.Scan(&month, &day); err != nil {
		fmt.Println("Invalid input.")
		return
	}

	date := NewSimpleDate(month, day)
	if date.IsValid() {
		fmt.Println("Valid date")
	} else {
		fmt.Println("Invalid date")
	}
}
