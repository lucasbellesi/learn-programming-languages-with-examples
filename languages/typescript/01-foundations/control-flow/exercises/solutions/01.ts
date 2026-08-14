import * as fs from "node:fs";
const choice = Number.parseInt(fs.readFileSync(0, "utf8").trim(), 10);
if (!Number.isInteger(choice)) {
    console.log("Expected one integer option.");
}
let label = "Unknown option";
switch (choice) {
    case 1:
        label = "Open";
        break;
    case 2:
        label = "Save";
        break;
    case 3:
        label = "Exit";
        break;
}
console.log(label);
