package main

import "fmt"

func runMemoryManagementRaiiExercise() {
	var depth int
	fmt.Scan(&depth)
	// TODO 1: Validate depth as a positive number of nested scopes.
	// TODO 2: Scope guard that proves nested cleanup order.
	// TODO 3: Produce enter/exit logs proving automatic cleanup; verify nested scopes; final active
	//         counter must return to zero.
	_ = depth
}

func main() {
	runMemoryManagementRaiiExercise()
}
