package main

import "fmt"

type Course struct {
	title    string
	capacity int
	enrolled int
}

func NewCourse(title string, capacity int) Course {
	if capacity < 0 {
		capacity = 0
	}
	return Course{title: title, capacity: capacity, enrolled: 0}
}

func (c *Course) Enroll() bool {
	if c.enrolled >= c.capacity {
		return false
	}
	c.enrolled++
	return true
}

func (c *Course) Drop() bool {
	if c.enrolled <= 0 {
		return false
	}
	c.enrolled--
	return true
}

func (c Course) PrintStatus() {
	fmt.Printf("Course: %s | %d/%d enrolled\n", c.title, c.enrolled, c.capacity)
}

func main() {
	goBasics := NewCourse("GoBasics", 2)
	algorithms := NewCourse("Algorithms", 3)

	goBasics.Enroll()
	goBasics.Enroll()
	goBasics.Enroll()

	algorithms.Enroll()

	goBasics.PrintStatus()
	algorithms.PrintStatus()
}
