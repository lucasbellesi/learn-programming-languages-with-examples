package main

import "fmt"

type node struct {
	name   string
	parent *node
	child  *node
}

func printChildName(parent *node) {
	if parent == nil || parent.child == nil {
		fmt.Println("Parent has no child.")
		return
	}
	fmt.Printf("Child name: %s\n", parent.child.name)
}

func printParentName(child *node) {
	if child == nil || child.parent == nil {
		fmt.Println("Child has no parent.")
		return
	}
	fmt.Printf("Parent name: %s\n", child.parent.name)
}

func main() {
	var scenario string
	fmt.Scan(&scenario)
	parent := &node{name: "parent"}
	child := &node{name: "child", parent: parent}
	parent.child = child

	switch scenario {
	case "linked":
		printChildName(parent)
		printParentName(child)
	case "parent-removed":
		child.parent = nil
		printParentName(child)
	case "child-removed":
		parent.child = nil
		printChildName(parent)
	}
}
