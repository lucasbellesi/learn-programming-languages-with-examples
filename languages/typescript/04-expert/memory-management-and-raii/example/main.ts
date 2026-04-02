// Module focus: Tying resource cleanup to object lifetime so cleanup stays predictable.
// Why it matters: practicing memory management and raii patterns makes exercises and checkpoints easier to reason about.

// Helper setup for memory management and raii; this keeps the walkthrough readable.
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

// Walk through one fixed scenario so memory management and raii behavior stays repeatable.
function main(): void {
    // Prepare sample inputs that exercise the key memory management and raii path.
    const report = new FakeFile("report.txt");

    usingResource(report, (handle) => {
        handle.writeLine("header");
        handle.writeLine("totals");
    });

    // Report values so learners can verify the memory management and raii outcome.
    console.log(`Closed after scope: ${report.isClosed()}`);
}

main();

export {};
