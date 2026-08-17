// Module focus: Modeling related data and behavior with structured types.
// Why it matters: the example makes it possible to model data and behavior with cohesive domain
// types before the learner tackles the exercises.

interface StudentRecord {
    // Interfaces capture data shape without adding behavior.
    name: string;
    score: number;
}

class CourseSummary {
    constructor(
        readonly title: string,
        readonly students: StudentRecord[],
    ) {}

    averageScore(): number {
        // Methods keep derived behavior close to the data they summarize.
        const total = this.students.reduce(
            (sum, student) => sum + student.score,
            0,
        );
        return total / this.students.length;
    }

    printSummary(): void {
        // The printed result shows whether the program can protect invariants through
        // constructors and methods.
        console.log(`Course: ${this.title}`);
        for (const student of this.students) {
            console.log(`- ${student.name}: ${student.score}`);
        }
        console.log(`Average: ${this.averageScore().toFixed(2)}`);
    }
}

// Build one realistic object so learners can inspect data plus behavior together.
const summary = new CourseSummary("TypeScript Core", [
    { name: "Ana", score: 91 },
    { name: "Bob", score: 77 },
    { name: "Carla", score: 88 },
]);

summary.printSummary();

export {};
