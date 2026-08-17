// Module focus: How names stay visible only inside the blocks that own them.
// Why it matters: the example makes it possible to predict name visibility across nested scopes
// before the learner tackles the exercises.

function makeCounter(start: number): () => number {
    let current = start;
    return () => {
        current += 1;
        return current;
    };
}
const nextTicket = makeCounter(100);
// The printed result shows whether the program can explain when values and resources cease to be
// usable.
console.log(`Ticket: ${nextTicket()}`);
console.log(`Ticket: ${nextTicket()}`);
{
    const label = "inner scope";
    console.log(`Scoped label: ${label}`);
}
export {};
