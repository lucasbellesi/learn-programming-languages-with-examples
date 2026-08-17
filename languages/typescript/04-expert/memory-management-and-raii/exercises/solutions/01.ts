import { readFileSync } from "node:fs";

class TemporaryBuffer {
    private released = false;

    constructor(readonly label: string) {
        console.log(`Acquire ${label}`);
    }

    append(chunk: string): void {
        if (this.released) {
            throw new Error("Buffer already released.");
        }
        console.log(`Append ${chunk}`);
    }

    release(): void {
        if (!this.released) {
            console.log(`Release ${this.label}`);
            this.released = true;
        }
    }
}

function main(): void {
    const [label = "buffer", chunkLine = "", mode = "success"] = readFileSync(
        0,
        "utf8",
    )
        .trimEnd()
        .split(/\r?\n/);
    const chunks = chunkLine
        .split(",")
        .map((chunk) => chunk.trim())
        .filter((chunk) => chunk.length > 0);
    const buffer = new TemporaryBuffer(label.trim() || "buffer");

    try {
        for (const chunk of chunks) {
            buffer.append(chunk);
        }
        if (mode.trim() === "failure") {
            throw new Error("Simulated failure after work");
        }
        console.log(`Work complete: ${chunks.length} chunk(s)`);
    } catch (error) {
        if (error instanceof Error) {
            console.log(`Caught: ${error.message}`);
        }
    } finally {
        buffer.release();
    }
}

main();

export {};
