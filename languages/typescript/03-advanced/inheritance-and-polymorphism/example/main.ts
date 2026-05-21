// Module focus: Treating different concrete types through one common interface.
// Why it matters: practicing inheritance and polymorphism patterns makes exercises and checkpoints easier to reason about.

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
    // Report output values so learners can verify the inheritance and polymorphism result.
    console.log(`${shape.name()}: ${shape.area().toFixed(2)}`);
}

export {};
