// This example shows tracking ownership and lifetime when multiple references can observe the same value.
// In Go, the example keeps the flow explicit through small functions, interfaces, and concrete data.

package main

import "fmt"

// Define the reusable pieces first so the main flow can focus on one observable scenario.
type report struct {
	title string
}

type reportOwner struct {
	name   string
	report *report
}

func (o *reportOwner) transferTo(destination *reportOwner) {
	if o.report == nil {
		fmt.Printf("%s has nothing to transfer.\n", o.name)
		return
	}
	fmt.Printf("%s transfers %s to %s.\n", o.name, o.report.title, destination.name)
	destination.report = o.report
	o.report = nil
}

func (o *reportOwner) print() {
	if o.report == nil {
		fmt.Printf("%s: empty\n", o.name)
		return
	}
	fmt.Printf("%s: %s\n", o.name, o.report.title)
}

// Run one deterministic scenario so the console output makes tracking ownership and lifetime when multiple references can observe the same value easy to verify.
func main() {
	// Build the sample state first, then let the later output confirm the behavior step by step.
	inbox := reportOwner{name: "Inbox", report: &report{title: "Quarterly Summary"}}
	archive := reportOwner{name: "Archive"}

	inbox.print()
	archive.print()
	inbox.transferTo(&archive)
	inbox.print()
	archive.print()

	score := 90
	primary := &score
	observer := primary
	*observer += 5

	// Print the observed state here so learners can connect the code path to a concrete result.
	fmt.Printf("Shared score after alias update: %d\n", score)
}
