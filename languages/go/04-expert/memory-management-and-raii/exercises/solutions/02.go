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

func main() {
	active := 0
	fmt.Printf("Active before scopes: %d\n", active)

	func() {
		outer := newScopeGuard("outer", &active)
		defer outer.Close()
		fmt.Printf("Active inside outer: %d\n", active)

		func() {
			inner := newScopeGuard("inner", &active)
			defer inner.Close()
			fmt.Printf("Active inside inner: %d\n", active)
		}()

		fmt.Printf("Active after inner: %d\n", active)
	}()

	fmt.Printf("Active after scopes: %d\n", active)
}
