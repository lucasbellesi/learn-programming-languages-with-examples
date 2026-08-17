package main

import (
	"bufio"
	"os"
)

func runSmartPointersInDepthExercise() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	sourceTitle := scanner.Text()
	scanner.Scan()
	destinationTitle := scanner.Text()
	// TODO 1: Convert `empty` to a nil holder and other lines to owned notes.
	// TODO 2: Move an owned note between holders.
	// TODO 3: Produce ownership transfer logs before and after moving; verify moving from an empty
	//         holder; destination already occupied.
	_ = sourceTitle
	_ = destinationTitle
}

func main() {
	runSmartPointersInDepthExercise()
}
