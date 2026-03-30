// Example purpose: adapt smart-pointer ideas to explicit pointer ownership and sharing in Go.

package main

import "fmt"

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

func main() {
	// Program flow: move one owned pointer, then show explicit shared mutation through aliases.
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

	// Intent: final output shows that shared pointer aliases mutate the same value.
	fmt.Printf("Shared score after alias update: %d\n", score)
}
