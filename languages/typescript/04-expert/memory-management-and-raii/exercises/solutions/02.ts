import { readFileSync } from "node:fs";

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

    close(): boolean {
        if (this.closed) {
            return false;
        }
        this.closed = true;
        return true;
    }
}

function main(): void {
    const session = new SessionLog();
    const commands = readFileSync(0, "utf8").split(/\r?\n/);

    for (const rawCommand of commands) {
        const command = rawCommand.trim();
        if (command.startsWith("record ")) {
            try {
                session.record(command.slice("record ".length));
            } catch (error) {
                if (error instanceof Error) {
                    console.log(`Guarded error: ${error.message}`);
                }
            }
        } else if (command === "close") {
            console.log(
                session.close() ? "Session closed." : "Session already closed.",
            );
        }
    }

    console.log(`Snapshot: ${session.snapshot() || "empty"}`);
}

main();

export {};
