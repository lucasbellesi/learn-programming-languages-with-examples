package main

import "fmt"

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
	active := noteHolder{label: "Active", item: &note{title: "Roadmap"}}
	backup := noteHolder{label: "Backup", item: &note{title: "Old Notes"}}
	empty := noteHolder{label: "Empty"}

	active.print()
	backup.print()
	active.moveTo(&backup)
	active.print()
	backup.print()
	empty.moveTo(&active)
	empty.print()
	active.print()
}
