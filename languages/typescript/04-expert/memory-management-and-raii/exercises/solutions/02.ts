class SessionLog {
    private readonly entries: string[] = [];
    private closed = false;

    record(entry: string): void {
        if (this.closed) {
            throw new Error("Cannot record after close.");
        }
        this.entries.push(entry);
    }

    snapshot(): string {
        return this.entries.join(", ");
    }

    close(): void {
        this.closed = true;
    }
}

function main(): void {
    const session = new SessionLog();
    session.record("connected");
    session.record("validated");

    console.log(`Before close: ${session.snapshot()}`);
    session.close();
    console.log("Session closed.");

    try {
        session.record("late-write");
    } catch (error) {
        if (error instanceof Error) {
            console.log(`Guarded error: ${error.message}`);
        }
    }
}

main();

export {};
