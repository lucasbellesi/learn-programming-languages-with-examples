import raw from "@/generated/catalog.json";
export type Case = {
    name: string;
    input_lines?: string[];
    [key: string]: unknown;
};
export type Activity = {
    id: string;
    title: string;
    path: string;
    source: string;
    kind: string;
    language: string;
    enabled: boolean;
    revision: string;
    cases: Case[];
    hints: string[];
    support?: { name: string; source: string }[];
};
export type Doc = {
    id: string;
    language: string;
    level: string;
    kind: string;
    title: string;
    markdown: string;
    path: string;
    activities: string[];
    files?: { path: string; source: string }[];
};
export const catalog = raw as unknown as {
    revision: string;
    docs: Doc[];
    activities: Record<string, Activity>;
};
export const languages: Record<string, string> = {
    cpp: "C++",
    csharp: "C#",
    go: "Go",
    java: "Java",
    python: "Python",
    typescript: "TypeScript",
};
export const levels: Record<string, string> = {
    "01-foundations": "Foundations",
    "02-core": "Core",
    "03-advanced": "Advanced",
    "04-expert": "Expert",
};
