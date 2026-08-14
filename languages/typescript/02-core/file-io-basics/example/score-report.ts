export type ScoreRecord = {
    name: string;
    score: number;
};

export function parseScoreRow(line: string): ScoreRecord | null {
    // Parse before touching the filesystem so malformed rows can be tested directly.
    const parts = line.trim().split(/\s+/);
    if (parts.length < 2) {
        return null;
    }

    const rawScore = parts.at(-1) ?? "";
    if (!/^[+-]?\d+$/.test(rawScore)) {
        return null;
    }
    const score = Number(rawScore);
    const name = parts.slice(0, -1).join(" ");
    return Number.isSafeInteger(score) && score >= 0 && score <= 100 && name
        ? { name, score }
        : null;
}

export function buildScoreReport(
    records: ScoreRecord[],
    invalidRows: number,
): string {
    const lines = [
        "Grade Report",
        `Valid records: ${records.length}`,
        `Invalid rows skipped: ${invalidRows}`,
    ];
    if (records.length === 0) {
        return [...lines, "No valid records."].join("\n");
    }

    const total = records.reduce((sum, record) => sum + record.score, 0);
    return [
        ...lines,
        `Average: ${(total / records.length).toFixed(2)}`,
        ...records.map((record) => `- ${record.name}: ${record.score}`),
    ].join("\n");
}
