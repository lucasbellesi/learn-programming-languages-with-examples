// This example shows tying resource cleanup to object lifetime so cleanup stays predictable.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

// Define the reusable pieces first so the main flow can focus on one observable scenario.
class FakeFile {
    private closed = false;

    constructor(readonly name: string) {
        console.log(`Opening ${name}`);
    }

    writeLine(line: string): void {
        this.ensureOpen();
        console.log(`writing: ${line}`);
    }

    close(): void {
        if (!this.closed) {
            console.log(`Closing ${this.name}`);
            this.closed = true;
        }
    }

    isClosed(): boolean {
        return this.closed;
    }

    private ensureOpen(): void {
        if (this.closed) {
            throw new Error("Resource already closed.");
        }
    }
}

function usingResource<T extends { close(): void }, TResult>(
    resource: T,
    work: (resource: T) => TResult,
): TResult {
    try {
        return work(resource);
    } finally {
        resource.close();
    }
}

// Run one deterministic scenario so the console output makes tying resource cleanup to object lifetime so cleanup stays predictable easy to verify.
function main(): void {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    const report = new FakeFile("report.txt");

    usingResource(report, (handle) => {
        handle.writeLine("header");
        handle.writeLine("totals");
    });

    // Print the observed state here so learners can connect the code path to a concrete result.
    console.log(`Closed after scope: ${report.isClosed()}`);
}

main();

export {};
