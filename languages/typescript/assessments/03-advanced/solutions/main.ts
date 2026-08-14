abstract class Shape {
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

function printList<T>(values: T[], label: string): void {
    console.log(
        `${label}: [${values.map((value) => String(value)).join(", ")}]`,
    );
}

function main(): void {
    const shapes: Shape[] = [
        new Circle(2),
        new Rectangle(3, 4),
        new Circle(1.5),
    ];
    const areas: number[] = [];

    console.log("Shape areas:");
    for (const shape of shapes) {
        const value = shape.area();
        areas.push(value);
        console.log(`- ${shape.name()}: ${value}`);
    }

    const totalArea = areas.reduce((sum, value) => sum + value, 0);
    const minimumArea = areas.reduce(
        (best, value) => Math.min(best, value),
        areas[0]!,
    );
    const maximumArea = areas.reduce(
        (best, value) => Math.max(best, value),
        areas[0]!,
    );

    console.log(`Total area: ${totalArea}`);
    console.log(`Minimum area: ${minimumArea}`);
    console.log(`Maximum area: ${maximumArea}`);

    printList([1, 2, 3, 4], "Sample counts");
    printList(areas, "Computed areas");
}

main();

export {};
