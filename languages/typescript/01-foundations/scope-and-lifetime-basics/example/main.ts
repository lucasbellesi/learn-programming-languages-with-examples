// Module focus: How names stay visible only inside the blocks that own them.
// Why it matters: practicing scope and lifetime basics patterns makes exercises and checkpoints easier to reason about.

function makeCounter(start: number): () => number {
    let current = start;
    return () => {
        current += 1;
        return current;
    };
}
const nextTicket = makeCounter(100);
// Report output values so learners can verify the scope and lifetime basics result.
console.log(`Ticket: ${nextTicket()}`);
console.log(`Ticket: ${nextTicket()}`);
{
    const label = "inner scope";
    console.log(`Scoped label: ${label}`);
}
export {};
