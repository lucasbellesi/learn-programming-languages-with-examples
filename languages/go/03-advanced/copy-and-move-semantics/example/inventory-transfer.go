// This extra example extends copy-and-move semantics with inventory transfer.
// Example purpose: contrast aliasing, cloning, and ownership-like transfer.

package main

import "fmt"

type Inventory struct {
	items []string
}

func NewInventory(items []string) Inventory {
	return Inventory{items: append([]string{}, items...)}
}

func (inventory Inventory) Clone() Inventory {
	return Inventory{items: append([]string{}, inventory.items...)}
}

func (inventory *Inventory) Transfer() Inventory {
	movedItems := inventory.items
	inventory.items = []string{}
	return Inventory{items: movedItems}
}

func main() {
	original := NewInventory([]string{"Notebook", "Pencil"})
	alias := &original
	clone := original.Clone()
	transferred := original.Transfer()

	alias.items = append(alias.items, "Marker")
	clone.items = append(clone.items, "Eraser")

	fmt.Printf("original items: %v\n", original.items)
	fmt.Printf("alias items: %v\n", alias.items)
	fmt.Printf("clone items: %v\n", clone.items)
	fmt.Printf("transferred items: %v\n", transferred.items)
}
