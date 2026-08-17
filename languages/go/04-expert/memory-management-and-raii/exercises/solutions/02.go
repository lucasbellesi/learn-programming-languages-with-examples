package main

import "fmt"

type scopeGuard struct {
	label  string
	active *int
	closed bool
}

func newScopeGuard(label string, active *int) *scopeGuard {
	*active += 1
	fmt.Printf("enter %s (active=%d)\n", label, *active)
	return &scopeGuard{label: label, active: active}
}

func (g *scopeGuard) Close() {
	if g.closed {
		return
	}
	g.closed = true
	*g.active -= 1
	fmt.Printf("exit %s (active=%d)\n", g.label, *g.active)
}

func runNestedScopes(depth, level int, active *int) {
	if level > depth {
		fmt.Printf("Active at deepest scope: %d\n", *active)
		return
	}
	guard := newScopeGuard(fmt.Sprintf("scope-%d", level), active)
	defer guard.Close()
	runNestedScopes(depth, level+1, active)
}

func main() {
	var depth int
	if _, err := fmt.Scan(&depth); err != nil || depth <= 0 {
		fmt.Println("Depth must be positive.")
		return
	}
	active := 0
	fmt.Printf("Active before scopes: %d\n", active)
	runNestedScopes(depth, 1, &active)
	fmt.Printf("Active after scopes: %d\n", active)
}
