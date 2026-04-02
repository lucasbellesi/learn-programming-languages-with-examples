// This example shows choosing between branches and repeating work with predictable control flow.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

const scores = [92, 74, 58];
for (const score of scores) {
    let label = "Needs support";
    if (score >= 85) {
        label = "Strong";
    } else if (score >= 60) {
        label = "Passing";
    }
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
