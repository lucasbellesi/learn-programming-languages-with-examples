package main

import (
	"bufio"
	"fmt"
	"os"
)

type note struct {
	title string
}

type noteHolder struct {
	label string
	item  *note
}

func (h *noteHolder) moveTo(destination *noteHolder) {
	if h.item == nil {
		fmt.Printf("%s is empty.\n", h.label)
		return
	}
	if destination.item != nil {
		fmt.Printf("%s is occupied.\n", destination.label)
		return
	}
	fmt.Printf("%s moves %s to %s.\n", h.label, h.item.title, destination.label)
	destination.item = h.item
	h.item = nil
}

func (h *noteHolder) print() {
	if h.item == nil {
		fmt.Printf("%s: empty\n", h.label)
		return
	}
	fmt.Printf("%s: %s\n", h.label, h.item.title)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	sourceTitle := scanner.Text()
	scanner.Scan()
	destinationTitle := scanner.Text()
	var sourceNote *note
	var destinationNote *note
	if sourceTitle != "empty" {
		sourceNote = &note{title: sourceTitle}
	}
	if destinationTitle != "empty" {
		destinationNote = &note{title: destinationTitle}
	}
	active := noteHolder{label: "Source", item: sourceNote}
	backup := noteHolder{label: "Destination", item: destinationNote}

	active.print()
	backup.print()
	active.moveTo(&backup)
	active.print()
	backup.print()
}
