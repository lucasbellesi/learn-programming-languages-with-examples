// Module focus: Tying resource cleanup to object lifetime so cleanup stays predictable.
// Why it matters: the example makes it possible to explain the language's resource and memory
// lifetime model before the learner tackles the exercises.

// Separate helpers keep the main path focused on how to explain the language's resource and
// memory lifetime model.
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

// Fixed inputs make the consequence of assuming garbage collection will close files or sockets
// for you visible and repeatable.
function main(): void {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    const report = new FakeFile("report.txt");

    usingResource(report, (handle) => {
        handle.writeLine("header");
        handle.writeLine("totals");
    });

    // The printed result shows whether the program can guarantee deterministic cleanup for
    // non-memory resources.
    console.log(`Closed after scope: ${report.isClosed()}`);
}

main();

export {};
