"use client";
import { useState } from "react";
import Link from "next/link";
const names: Record<string, string> = {
    cpp: "C++",
    csharp: "C#",
    go: "Go",
    java: "Java",
    python: "Python",
    typescript: "TypeScript",
};
const levelNames: Record<string, string> = {
    "01-foundations": "Foundations",
    "02-core": "Core",
    "03-advanced": "Advanced",
    "04-expert": "Expert",
};
type Item = {
    id: string;
    language: string;
    level: string;
    kind: string;
    title: string;
};
export function Explorer({ docs }: { docs: Item[] }) {
    const [language, setLanguage] = useState("python");
    const [query, setQuery] = useState("");
    const [level, setLevel] = useState("01-foundations");
    const items = docs.filter(
        (d) =>
            d.language === language &&
            d.level === level &&
            `${d.title} ${d.id}`.toLowerCase().includes(query.toLowerCase()),
    );
    return (
        <section id="curriculum" className="curriculum">
            <div className="section-heading">
                <div>
                    <span className="eyebrow">YOUR NEXT CHAPTER</span>
                    <h2>Choose your language.</h2>
                    <p>Same concepts. Different ways to express them.</p>
                </div>
                <label className="search">
                    ⌕{" "}
                    <input
                        aria-label="Search concepts"
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                        placeholder="Search concepts…"
                    />
                </label>
            </div>
            <div className="language-grid">
                {Object.entries(names).map(([key, name]) => (
                    <button
                        key={key}
                        aria-pressed={key === language}
                        onClick={() => setLanguage(key)}
                        className={`language ${key === language ? "selected" : ""}`}
                    >
                        <span className={`language-icon ${key}`}>
                            {key === "typescript"
                                ? "TS"
                                : key === "python"
                                  ? "Py"
                                  : name}
                        </span>
                        <strong>{name}</strong>
                        <span>
                            24 concepts <span aria-hidden>↗</span>
                        </span>
                    </button>
                ))}
            </div>
            <div className="level-tabs">
                {Object.entries(levelNames).map(([key, name], i) => (
                    <button
                        key={key}
                        aria-pressed={level === key}
                        onClick={() => setLevel(key)}
                    >
                        <span>0{i + 1}</span> {name}
                    </button>
                ))}
            </div>
            <div className="module-heading">
                <h3>{levelNames[level]}</h3>
                <span>
                    {level === "01-foundations"
                        ? "Examples & exercises ready to run"
                        : "Read, explore & download · online execution coming later"}
                </span>
            </div>
            <div className="module-grid">
                {items.map((doc, i) => (
                    <Link
                        key={doc.id}
                        className="module-card"
                        href={`/learn/${doc.id}`}
                    >
                        <span className="module-number">
                            {String(i + 1).padStart(2, "0")}
                        </span>
                        <div>
                            <span className="card-kind">{doc.kind}</span>
                            <h3>{doc.title.replace(/^.*?: /, "")}</h3>
                            <span className="muted">
                                {doc.kind === "module"
                                    ? "Example + 2 guided exercises"
                                    : "Starter files & review guidance"}
                            </span>
                        </div>
                        <span className="arrow">↗</span>
                    </Link>
                ))}
            </div>
            {!items.length && <p>No concepts match this search.</p>}
            <aside className="practice-note">
                <strong>No setup needed for your first step.</strong>
                <p>
                    Read freely, save your drafts on this device, and try
                    foundations exercises online. Free execution has daily
                    limits.
                </p>
            </aside>
        </section>
    );
}
