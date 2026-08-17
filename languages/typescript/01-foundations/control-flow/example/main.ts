// Module focus: Choosing between branches and repeating work with predictable control flow.
// Why it matters: the example makes it possible to select branches that cover normal and boundary
// conditions before the learner tackles the exercises.

const scores = [92, 74, 58];
for (const score of scores) {
    // Start with the fallback label, then let stronger cases override it.
    let label = "Needs support";
    if (score >= 85) {
        label = "Strong";
    } else if (score >= 60) {
        label = "Passing";
    }
    // The printed result shows whether the program can write terminating loops and reason about
    // their invariants.
    console.log(`Score ${score}: ${label}`);
}
const menuChoice: number = 2;
// A switch is useful when one value maps to several named actions.
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
