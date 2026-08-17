// Module focus: Tracking ownership and lifetime when multiple references can observe the same value.
// Why it matters: the example makes it possible to model exclusive, shared, and non-owning
// relationships idiomatically before the learner tackles the exercises.

package main

import "fmt"

// Separate helpers keep the main path focused on how to model exclusive, shared, and non-owning
// relationships idiomatically.
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

// Fixed inputs make the consequence of using pointers everywhere even when values are simpler
// visible and repeatable.
func main() {
	// These values exercise the normal path before the exercises vary the documented boundaries.
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

	// The printed result shows whether the program can prevent leaks, cycles, and stale observations
	// in ownership graphs.
	fmt.Printf("Shared score after alias update: %d\n", score)
}
