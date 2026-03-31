import * as fs from "node:fs";

type StudentRecord = {
    name: string;
    score: number;
};

const lines = fs
    .readFileSync(0, "utf8")
    .split(/\r?\n/)
    .map((line) => line.trimEnd())
    .filter((line) => line.length > 0);

let index = 0;

function nextLine(): string {
    if (index >= lines.length) {
        throw new Error("Missing input line.");
    }
    return lines[index++]!;
}

function readPositiveCount(): number {
    while (true) {
        const value = Number.parseInt(nextLine(), 10);
        if (Number.isInteger(value) && value > 0) {
            return value;
        }
        console.log("Invalid student count. Enter a positive integer.");
    }
}

function readScore(name: string): number {
    while (true) {
        const value = Number.parseInt(nextLine(), 10);
        if (Number.isInteger(value) && value >= 0 && value <= 100) {
            return value;
        }
        console.log(
            `Invalid score for ${name}. Enter a value between 0 and 100.`,
        );
    }
}

const studentCount = readPositiveCount();
const students: StudentRecord[] = [];

for (let current = 0; current < studentCount; current += 1) {
    const name = nextLine();
    const score = readScore(name);
    students.push({ name, score });
}

const total = students.reduce((sum, student) => sum + student.score, 0);
const minimum = students.reduce(
    (best, student) => Math.min(best, student.score),
    students[0]!.score,
);
const maximum = students.reduce(
    (best, student) => Math.max(best, student.score),
    students[0]!.score,
);

console.log("Students:");
for (const student of students) {
    console.log(`- ${student.name}: ${student.score}`);
}
console.log(`Average: ${(total / students.length).toFixed(2)}`);
console.log(`Minimum: ${minimum}`);
console.log(`Maximum: ${maximum}`);
