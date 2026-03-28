// This extra example extends formatted output with a compact score report.
// Example purpose: align labels, numbers, and a final summary row.

package main

import "fmt"

type studentRow struct {
	name  string
	score int
	tasks int
}

func main() {
	rows := []studentRow{
		{"Ana", 91, 4},
		{"Bruno", 77, 3},
		{"Carla", 88, 5},
	}

	fmt.Printf("%-10s%8s%8s%10s\n", "Student", "Score", "Tasks", "Average")
	fmt.Println("------------------------------------")

	weightedTotal := 0
	taskTotal := 0
	for _, row := range rows {
		average := float64(row.score) / float64(row.tasks)
		weightedTotal += row.score
		taskTotal += row.tasks
		fmt.Printf("%-10s%8d%8d%10.2f\n", row.name, row.score, row.tasks, average)
	}

	fmt.Println("------------------------------------")
	fmt.Printf("%-10s%8d%8d%10.2f\n", "Totals", weightedTotal, taskTotal, float64(weightedTotal)/float64(taskTotal))
}
