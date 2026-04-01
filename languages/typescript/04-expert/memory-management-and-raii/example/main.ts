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

function main(): void {
    // Intent: make cleanup explicit even though the language has garbage collection.
    const report = new FakeFile("report.txt");

    usingResource(report, (handle) => {
        handle.writeLine("header");
        handle.writeLine("totals");
    });

    console.log(`Closed after scope: ${report.isClosed()}`);
}

main();

export {};
