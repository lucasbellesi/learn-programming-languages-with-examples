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
	parent := &node{name: "parent"}
	child := &node{name: "child", parent: parent}
	parent.child = child

	printChildName(parent)
	printParentName(child)

	parent.child = nil
	printChildName(parent)
	printParentName(child)
}
