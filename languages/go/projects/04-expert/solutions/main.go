package main

import (
	"fmt"
	"time"
)

type Step struct {
	name           string
	processedCount int
}

func NewStep(name string) *Step {
	return &Step{name: name, processedCount: 0}
}

func (s *Step) Run() {
	s.processedCount++
}

func main() {
	const jobCount = 3

	steps := []*Step{
		NewStep("load"),
		NewStep("transform"),
	}

	start := time.Now()

	for job := 0; job < jobCount; job++ {
		for _, step := range steps {
			step.Run()
		}
	}

	elapsed := time.Since(start).Microseconds()

	fmt.Printf("Running %d jobs through %d steps...\n", jobCount, len(steps))
	for _, step := range steps {
		fmt.Printf("Step %s processed %d jobs\n", step.name, step.processedCount)
	}
	fmt.Printf("Elapsed (microseconds): %d\n", elapsed)
}
