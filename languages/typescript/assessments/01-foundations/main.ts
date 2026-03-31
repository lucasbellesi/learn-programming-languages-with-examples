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

if (lines.length === 0) {
    console.log("Expected an assessment input payload.");
}

const count = Number.parseInt(lines[0]!, 10);
if (!Number.isInteger(count) || count <= 0) {
    console.log("Student count must be a positive integer.");
}

const students: StudentRecord[] = [];
let index = 1;
for (let current = 0; current < count; current += 1) {
    const name = lines[index++] ?? "";
    const score = Number.parseInt(lines[index++] ?? "", 10);
    if (!name || !Number.isInteger(score) || score < 0 || score > 100) {
        console.log("Invalid student record.");
    }
    students.push({ name, score });
}

const total = students.reduce((sum, student) => sum + student.score, 0);
const highest = students.reduce(
    (best, student) => (student.score > best.score ? student : best),
    students[0]!,
);
const lowest = students.reduce(
    (best, student) => (student.score < best.score ? student : best),
    students[0]!,
);
const passed = students.filter((student) => student.score >= 60).length;

console.log("Students:");
for (const student of students) {
    console.log(`- ${student.name}: ${student.score}`);
}
console.log(`Average: ${(total / students.length).toFixed(2)}`);
console.log(`Highest: ${highest.name} (${highest.score})`);
console.log(`Lowest: ${lowest.name} (${lowest.score})`);
console.log(`Passed: ${passed}/${students.length}`);
