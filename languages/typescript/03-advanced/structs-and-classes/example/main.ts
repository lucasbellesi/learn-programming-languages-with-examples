// Module focus: Modeling related data and behavior with structured types.
// Why it matters: practicing structs and classes patterns makes exercises and checkpoints easier to reason about.

interface StudentRecord {
    name: string;
    score: number;
}

class CourseSummary {
    constructor(
        readonly title: string,
        readonly students: StudentRecord[],
    ) {}

    averageScore(): number {
        const total = this.students.reduce(
            (sum, student) => sum + student.score,
            0,
        );
        return total / this.students.length;
    }

    printSummary(): void {
        // Report output values so learners can verify the structs and classes result.
        console.log(`Course: ${this.title}`);
        for (const student of this.students) {
            console.log(`- ${student.name}: ${student.score}`);
        }
        console.log(`Average: ${this.averageScore().toFixed(2)}`);
    }
}

const summary = new CourseSummary("TypeScript Core", [
    { name: "Ana", score: 91 },
    { name: "Bob", score: 77 },
    { name: "Carla", score: 88 },
]);

summary.printSummary();

export {};
