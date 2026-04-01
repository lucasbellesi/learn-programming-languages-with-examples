class Course {
    #enrolled = 0;

    constructor(
        readonly title: string,
        readonly capacity: number,
    ) {
        if (!title.trim()) {
            throw new Error("Course title is required.");
        }
        if (!Number.isInteger(capacity) || capacity < 0) {
            throw new Error("Capacity must be a non-negative integer.");
        }
    }

    enroll(): boolean {
        if (this.#enrolled >= this.capacity) {
            return false;
        }
        this.#enrolled += 1;
        return true;
    }

    drop(): boolean {
        if (this.#enrolled <= 0) {
            return false;
        }
        this.#enrolled -= 1;
        return true;
    }

    printStatus(): void {
        console.log(
            `Course: ${this.title} | ${this.#enrolled}/${this.capacity} enrolled`,
        );
    }
}

function main(): void {
    const typescriptBasics = new Course("TypeScriptBasics", 2);
    const algorithms = new Course("Algorithms", 3);

    typescriptBasics.enroll();
    typescriptBasics.enroll();
    typescriptBasics.enroll();

    algorithms.enroll();

    typescriptBasics.printStatus();
    algorithms.printStatus();
}

main();

export {};
