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
    const buffer = new TemporaryBuffer("session-cache");

    try {
        buffer.append("header");
        buffer.append("payload");
        throw new Error("Simulated failure after work");
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
