"use client";
import { useState } from "react";
import Link from "next/link";
import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeSanitize from "rehype-sanitize";
import rehypeSlug from "rehype-slug";
import type { Activity, Doc } from "@/lib/catalog";
import { Practice } from "./practice";
const languages: Record<string, string> = {
    cpp: "C++",
    csharp: "C#",
    go: "Go",
    java: "Java",
    python: "Python",
    typescript: "TypeScript",
};
const repo =
    "https://github.com/lucasbellesi/learn-programming-languages-with-examples";
function hrefFor(href: string | undefined, path: string, revision: string) {
    if (!href) return "#";
    if (href.startsWith("#") || /^https?:/.test(href)) return href;
    const url = new URL(href, `https://curriculum.local/${path}`);
    const parts = url.pathname.slice(1).split("/");
    if (
        parts[0] === "languages" &&
        parts.at(-1) === "README.md" &&
        parts.length === 5
    ) {
        const [, lang, level, concept] = parts;
        const id = ["projects", "assessments"].includes(level)
            ? `${lang}/${concept}/${level.slice(0, -1)}`
            : `${lang}/${level}/${concept}`;
        return `/learn/${id}${url.hash}`;
    }
    return `${repo}/blob/${revision}${url.pathname}${url.hash}`;
}
export function download(filename: string, source: string) {
    const url = URL.createObjectURL(
        new Blob([source], { type: "text/plain;charset=utf-8" }),
    );
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    a.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
}
export function Lesson({
    doc,
    activities,
    revision,
}: {
    doc: Doc;
    activities: Activity[];
    revision: string;
}) {
    const [tab, setTab] = useState("read");
    const [width, setWidth] = useState(44);
    return (
        <>
            <div className="lesson-heading">
                <div>
                    <span className="eyebrow">
                        {doc.kind} · {languages[doc.language]}
                    </span>
                    <h1>{doc.title}</h1>
                </div>
                <label>
                    See this concept in
                    <select
                        aria-label="Language for this concept"
                        value={doc.language}
                        onChange={(e) => {
                            location.href = `/learn/${[e.target.value, ...doc.id.split("/").slice(1)].join("/")}`;
                        }}
                    >
                        {Object.entries(languages).map(([id, name]) => (
                            <option key={id} value={id}>
                                {name}
                            </option>
                        ))}
                    </select>
                </label>
            </div>
            <div className="mobile-tabs">
                <button
                    aria-pressed={tab === "read"}
                    onClick={() => setTab("read")}
                >
                    Read
                </button>
                <button
                    aria-pressed={tab === "practice"}
                    onClick={() => setTab("practice")}
                >
                    Practice
                </button>
            </div>
            <div
                className="workspace"
                style={
                    { "--reading-width": `${width}%` } as React.CSSProperties
                }
            >
                <article
                    className={`reading ${tab === "read" ? "mobile-active" : ""}`}
                >
                    <Markdown
                        remarkPlugins={[remarkGfm]}
                        rehypePlugins={[rehypeSanitize, rehypeSlug]}
                        components={{
                            a: ({ href, children }) => (
                                <a href={hrefFor(href, doc.path, revision)}>
                                    {children}
                                </a>
                            ),
                            img: () => null,
                        }}
                    >
                        {doc.markdown.replace(/^# .+\r?\n/, "")}
                    </Markdown>
                    <p className="revision">
                        Content revision{" "}
                        <a href={`${repo}/commit/${revision}`}>
                            {revision.slice(0, 7)}
                        </a>
                    </p>
                </article>
                <div className="resizer">
                    <label>
                        Reading panel width
                        <input
                            type="range"
                            min="25"
                            max="65"
                            value={width}
                            onChange={(e) => setWidth(Number(e.target.value))}
                        />
                    </label>
                </div>
                <section
                    className={`practice ${tab === "practice" ? "mobile-active" : ""}`}
                    aria-label="Code practice"
                >
                    {activities.length ? (
                        <Practice key={doc.id} activities={activities} />
                    ) : (
                        <div className="checkpoint">
                            <span className="eyebrow">READ & DOWNLOAD</span>
                            <h2>Take the next step locally.</h2>
                            <p>
                                Online execution for projects and assessments is
                                coming later. Download the starter files and
                                follow the instructions alongside your editor.
                            </p>
                            {doc.files?.map((file) => (
                                <div key={file.path}>
                                    <button
                                        onClick={() =>
                                            download(
                                                file.path.split("/").at(-1)!,
                                                file.source,
                                            )
                                        }
                                    >
                                        Download {file.path.split("/").at(-1)} ↓
                                    </button>
                                    <details>
                                        <summary>View source</summary>
                                        <pre>{file.source}</pre>
                                    </details>
                                </div>
                            ))}
                        </div>
                    )}
                </section>
            </div>
            <div className="lesson-end">
                <Link href="/">← Back to the curriculum</Link>
                <span>Your next insight is one experiment away.</span>
            </div>
        </>
    );
}
