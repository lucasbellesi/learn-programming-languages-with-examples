// Module focus: Choosing between branches and repeating work with predictable control flow.
// Why it matters: practicing control flow patterns makes exercises and checkpoints easier to reason about.

const scores = [92, 74, 58];
for (const score of scores) {
    let label = "Needs support";
    if (score >= 85) {
        label = "Strong";
    } else if (score >= 60) {
        label = "Passing";
    }
    // Report output values so learners can verify the control flow result.
    console.log(`Score ${score}: ${label}`);
}
const menuChoice: number = 2;
switch (menuChoice) {
    case 1:
        console.log("Menu: Create report");
        break;
    case 2:
        console.log("Menu: View summary");
        break;
    default:
        console.log("Menu: Unknown option");
        break;
}
export {};
