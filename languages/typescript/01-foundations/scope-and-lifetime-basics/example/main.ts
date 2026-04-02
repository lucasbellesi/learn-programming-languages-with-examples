// This example shows how names stay visible only inside the blocks that own them.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

function makeCounter(start: number): () => number {
    let current = start;
    return () => {
        current += 1;
        return current;
    };
}
const nextTicket = makeCounter(100);
console.log(`Ticket: ${nextTicket()}`);
console.log(`Ticket: ${nextTicket()}`);
{
    const label = "inner scope";
    console.log(`Scoped label: ${label}`);
}
export {};
