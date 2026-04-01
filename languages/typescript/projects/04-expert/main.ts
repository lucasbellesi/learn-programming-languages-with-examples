import { performance } from "node:perf_hooks";
import { setTimeout as delay } from "node:timers/promises";

type Job = {
    id: number;
    payload: string;
};

class AuditLog {
    private readonly entries: string[] = [];
    private closed = false;

    append(entry: string): void {
        if (this.closed) {
            throw new Error("Audit log is closed.");
        }
        this.entries.push(entry);
    }

    close(): void {
        this.closed = true;
    }

    isClosed(): boolean {
        return this.closed;
    }
}

class PipelineStep {
    processedCount = 0;

    constructor(
        readonly name: string,
        private readonly delayMs: number,
    ) {}

    async run(job: Job, log: AuditLog): Promise<void> {
        await delay(this.delayMs);
        this.processedCount += 1;
        log.append(`${this.name}:${job.id}:${job.payload}`);
    }
}

async function main(): Promise<void> {
    const jobs: Job[] = [
        { id: 101, payload: "alpha" },
        { id: 102, payload: "beta" },
        { id: 103, payload: "gamma" },
    ];
    const steps = [
        new PipelineStep("load", 6),
        new PipelineStep("transform", 4),
    ];
    const auditLog = new AuditLog();
    const start = performance.now();

    try {
        await Promise.all(
            jobs.map(async (job) => {
                for (const step of steps) {
                    await step.run(job, auditLog);
                }
            }),
        );
    } finally {
        auditLog.close();
    }

    const elapsedMs = performance.now() - start;

    console.log(`Running ${jobs.length} jobs through ${steps.length} steps...`);
    for (const step of steps) {
        console.log(`Step ${step.name} processed ${step.processedCount} jobs`);
    }
    console.log(`Elapsed (ms): ${elapsedMs.toFixed(2)}`);
    console.log(`Report closed: ${auditLog.isClosed()}`);
}

main().catch((error: unknown) => {
    if (error instanceof Error) {
        console.error(error.message);
    } else {
        console.error("Unknown error");
    }
    process.exitCode = 1;
});
