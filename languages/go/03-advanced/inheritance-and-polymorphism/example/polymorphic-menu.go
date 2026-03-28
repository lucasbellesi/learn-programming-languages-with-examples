// This extra example extends inheritance-and-polymorphism with a polymorphic menu.
// Example purpose: collect different shapes behind one shared interface.

package main

import "fmt"

type shape interface {
	area() float64
	name() string
}

type circle struct {
	radius float64
}

func (current circle) area() float64 {
	return 3.1415926535 * current.radius * current.radius
}

func (current circle) name() string {
	return "Circle"
}

type rectangle struct {
	width  float64
	height float64
}

func (current rectangle) area() float64 {
	return current.width * current.height
}

func (current rectangle) name() string {
	return "Rectangle"
}

func main() {
	shapes := make([]shape, 0)

	for {
		fmt.Println("\nMenu")
		fmt.Println("1) Add circle")
		fmt.Println("2) Add rectangle")
		fmt.Println("3) List areas")
		fmt.Println("4) Exit")
		fmt.Print("Choose: ")

		var option int
		if _, err := fmt.Scan(&option); err != nil {
			fmt.Println("Invalid option.")
			return
		}

		switch option {
		case 1:
			var radius float64
			fmt.Print("Radius: ")
			if _, err := fmt.Scan(&radius); err != nil || radius <= 0.0 {
				fmt.Println("Radius must be positive.")
				continue
			}
			shapes = append(shapes, circle{radius: radius})
		case 2:
			var width float64
			var height float64
			fmt.Print("Width: ")
			if _, err := fmt.Scan(&width); err != nil {
				fmt.Println("Width and height must be positive.")
				continue
			}
			fmt.Print("Height: ")
			if _, err := fmt.Scan(&height); err != nil || width <= 0.0 || height <= 0.0 {
				fmt.Println("Width and height must be positive.")
				continue
			}
			shapes = append(shapes, rectangle{width: width, height: height})
		case 3:
			if len(shapes) == 0 {
				fmt.Println("No shapes added yet.")
				continue
			}

			totalArea := 0.0
			for _, current := range shapes {
				shapeArea := current.area()
				totalArea += shapeArea
				fmt.Printf("- %s area: %v\n", current.name(), shapeArea)
			}
			fmt.Printf("Total area: %v\n", totalArea)
		case 4:
			fmt.Println("Goodbye.")
			return
		default:
			fmt.Println("Invalid option.")
		}
	}
}
