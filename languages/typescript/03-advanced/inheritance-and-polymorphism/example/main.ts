// Module focus: Treating different concrete types through one common interface.
// Why it matters: the example makes it possible to program against a shared behavioral
// abstraction before the learner tackles the exercises.

abstract class Shape {
    // The base type defines the behavior the loop can depend on.
    abstract name(): string;
    abstract area(): number;
}

class Circle extends Shape {
    constructor(readonly radius: number) {
        super();
    }

    name(): string {
        return "Circle";
    }

    area(): number {
        return Math.PI * this.radius * this.radius;
    }
}

class Rectangle extends Shape {
    constructor(
        readonly width: number,
        readonly height: number,
    ) {
        super();
    }

    name(): string {
        return "Rectangle";
    }

    area(): number {
        return this.width * this.height;
    }
}

const shapes: Shape[] = [new Circle(2), new Rectangle(3, 4)];
// The loop does not branch on concrete type; each object supplies its own area.
for (const shape of shapes) {
    // The printed result shows whether the program can use dynamic dispatch without unsafe type
    // assumptions.
    console.log(`${shape.name()}: ${shape.area().toFixed(2)}`);
}

export {};
