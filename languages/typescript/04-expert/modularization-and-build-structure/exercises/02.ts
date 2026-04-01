type EventSummary = {
    event: string;
    count: number;
};

function parseEvents(lines: string[]): EventSummary[] {
    const counts = new Map<string, number>();

    for (const line of lines) {
        const trimmed = line.trim();
        if (trimmed.length === 0) {
            continue;
        }

        counts.set(trimmed, (counts.get(trimmed) ?? 0) + 1);
    }

    return Array.from(counts.entries()).map(([event, count]) => ({
        event,
        count,
    }));
}

function renderSummary(summaries: EventSummary[]): string {
    return summaries
        .map((summary) => `${summary.event}: ${summary.count}`)
        .join("\n");
}

function main(): void {
    const summaries = parseEvents([
        "login",
        "purchase",
        "login",
        "logout",
        "",
        "purchase",
    ]);

    console.log(renderSummary(summaries));
}

main();

export {};
