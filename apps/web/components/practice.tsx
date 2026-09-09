"use client";
import dynamic from "next/dynamic";
import { useEffect, useRef, useState } from "react";
import type { Activity } from "@/lib/catalog";
import { loadDraft, saveDraft } from "@/lib/browser-db";
import { download } from "./lesson";
const Editor = dynamic(
    async () => {
        const module = await import("@monaco-editor/react");
        module.loader.config({ paths: { vs: "/monaco/vs" } });
        return module.default;
    },
    {
        ssr: false,
        loading: () => <p className="editor-loading">Loading your editor…</p>,
    },
);
type Result = {
    id?: string;
    status: string;
    message?: string;
    cases?: {
        name: string;
        input: string;
        expected: string;
        stdout: string;
        stderr: string;
        passed: boolean;
        message?: string;
    }[];
    compilation?: string;
};
const editorLanguages: Record<string, string> = {
    cpp: "cpp",
    csharp: "csharp",
    go: "go",
    java: "java",
    python: "python",
    typescript: "typescript",
};
export function Practice({ activities }: { activities: Activity[] }) {
    const [selected, setSelected] = useState(0);
    const activity = activities[selected];
    const [code, setCode] = useState(activity.source);
    const [stdin, setStdin] = useState("");
    const [ready, setReady] = useState(false);
    const [completed, setCompleted] = useState(false);
    const [saved, setSaved] = useState("Loading draft…");
    const [hint, setHint] = useState(0);
    const [solution, setSolution] = useState("");
    const [result, setResult] = useState<Result>();
    const [busy, setBusy] = useState(false);
    const [capability, setCapability] = useState(
        "Checking execution availability…",
    );
    const [canRun, setCanRun] = useState(false);
    const generation = useRef(0);
    const runId = useRef<string | undefined>(undefined);
    const currentCode = useRef(code);
    currentCode.current = code;
    useEffect(() => {
        fetch("/api/capabilities")
            .then((r) => r.json())
            .then((d) => {
                setCanRun(d.execution);
                setCapability(d.message);
            })
            .catch(() =>
                setCapability(
                    "Execution is unavailable. You can still edit and download.",
                ),
            );
    }, []);
    useEffect(() => {
        let active = true;
        setReady(false);
        setHint(0);
        setSolution("");
        setResult(undefined);
        setStdin(activity.cases[0]?.input_lines?.join("\n") ?? "");
        loadDraft(activity.id)
            .then((d) => {
                if (active) {
                    setCode(d?.code ?? activity.source);
                    setCompleted(
                        Boolean(d?.passed && d.revision === activity.revision),
                    );
                    setSaved(
                        d && d.revision !== activity.revision
                            ? "Saved draft from an earlier content revision"
                            : "Saved on this device",
                    );
                    setReady(true);
                }
            })
            .catch(() => {
                if (active) {
                    setCode(activity.source);
                    setSaved(
                        "Browser storage unavailable. Download to keep your work.",
                    );
                    setReady(true);
                }
            });
        return () => {
            active = false;
        };
    }, [activity]);
    useEffect(() => {
        if (!ready) return;
        setSaved("Saving…");
        const timer = setTimeout(() => {
            saveDraft({
                id: activity.id,
                code,
                revision: activity.revision,
                updatedAt: new Date().toISOString(),
                passed: completed,
            })
                .then(() => setSaved("Saved on this device"))
                .catch(() => setSaved("Could not save. Download your code."));
        }, 300);
        return () => clearTimeout(timer);
    }, [activity, code, ready, completed]);
    useEffect(() => {
        const warn = (event: BeforeUnloadEvent) => {
            if (
                saved === "Saving…" ||
                saved.includes("Could not save") ||
                busy
            ) {
                event.preventDefault();
                event.returnValue = "";
            }
        };
        window.addEventListener("beforeunload", warn);
        const navigate = (event: MouseEvent) => {
            const link = (event.target as HTMLElement).closest("a");
            if (
                link &&
                !link.hash &&
                (saved === "Saving…" || busy) &&
                !confirm(
                    "Leave this exercise before the pending save or execution finishes?",
                )
            ) {
                event.preventDefault();
                event.stopPropagation();
            }
        };
        document.addEventListener("click", navigate, true);
        return () => {
            window.removeEventListener("beforeunload", warn);
            document.removeEventListener("click", navigate, true);
        };
    }, [saved, busy]);
    async function select(index: number) {
        const persisted = await saveDraft({
            id: activity.id,
            code: currentCode.current,
            revision: activity.revision,
            updatedAt: new Date().toISOString(),
            passed: completed,
        })
            .then(() => true)
            .catch(() => false);
        if (
            !persisted &&
            !confirm(
                "Your draft could not be saved. Switch activities and discard these edits?",
            )
        )
            return;
        setSelected(index);
    }
    async function execute(mode: "run" | "check") {
        const token = ++generation.current;
        setBusy(true);
        setResult({ status: "starting" });
        runId.current = undefined;
        try {
            let response = await fetch("/api/executions", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    activityId: activity.id,
                    revision: activity.revision,
                    code,
                    stdin,
                    mode,
                    key: crypto.randomUUID(),
                }),
            });
            let next = await response.json();
            if (!response.ok)
                throw Error(next.message ?? "Execution is unavailable.");
            runId.current = next.id;
            while (token === generation.current) {
                setResult(next);
                if (!["starting", "compiling", "running"].includes(next.status))
                    break;
                await new Promise((r) => setTimeout(r, 900));
                response = await fetch(`/api/executions/${next.id}`);
                next = await response.json();
                if (!response.ok)
                    throw Error(
                        next.message ?? "Could not retrieve this execution.",
                    );
            }
            if (
                token === generation.current &&
                mode === "check" &&
                next.status === "passed"
            )
                setCompleted(true);
        } catch (error) {
            if (token === generation.current)
                setResult({
                    status: "unavailable",
                    message:
                        error instanceof Error
                            ? error.message
                            : "Execution unavailable.",
                });
        } finally {
            if (token === generation.current) setBusy(false);
        }
    }
    async function cancel() {
        if (!runId.current) return;
        try {
            const response = await fetch(`/api/executions/${runId.current}`, {
                method: "DELETE",
            });
            if (!response.ok) throw Error();
            generation.current++;
            setBusy(false);
            setResult({ status: "cancelled" });
        } catch {
            setResult((r) => ({
                ...r!,
                message:
                    "Cancellation could not be confirmed. The execution will stop at its time limit.",
            }));
        }
    }
    async function reveal() {
        const response = await fetch(
            `/api/solution?id=${encodeURIComponent(activity.id)}`,
        );
        if (response.ok) setSolution((await response.json()).source);
        else setSolution("Solution could not be loaded. Please try again.");
    }
    return (
        <>
            <div
                className="activity-tabs"
                role="tablist"
                aria-label="Practice activity"
            >
                {activities.map((a, i) => (
                    <button
                        role="tab"
                        aria-selected={selected === i}
                        disabled={busy}
                        onClick={() => select(i)}
                        key={a.id}
                    >
                        {a.title}
                    </button>
                ))}
            </div>
            <div className="editor-top">
                <span>{activity.path.split("/").at(-1)}</span>
                <span role="status">{saved}</span>
            </div>
            <div className="editor-shell">
                <Editor
                    height="440px"
                    language={editorLanguages[activity.language]}
                    theme="vs-dark"
                    value={code}
                    onChange={(value) => {
                        setCode(value ?? "");
                        setCompleted(false);
                    }}
                    options={{
                        fontSize: 14,
                        minimap: { enabled: false },
                        scrollBeyondLastLine: false,
                        padding: { top: 18 },
                        automaticLayout: true,
                        tabSize: 4,
                        readOnly: !ready || busy,
                        ariaLabel: "Code editor",
                        accessibilitySupport: "on",
                        editContext: false,
                    }}
                />
            </div>
            <div className="editor-actions">
                <button
                    className="primary"
                    disabled={!activity.enabled || !canRun || busy || !ready}
                    onClick={() => execute("run")}
                >
                    ▶ Run code
                </button>
                {activity.kind === "exercise" && (
                    <button
                        disabled={
                            !activity.enabled || !canRun || busy || !ready
                        }
                        onClick={() => execute("check")}
                    >
                        Check exercise
                    </button>
                )}
                <button disabled={!busy || !runId.current} onClick={cancel}>
                    Stop
                </button>
                <button
                    disabled={busy}
                    onClick={() => {
                        if (
                            confirm(
                                "Replace your current code with the original starter?",
                            )
                        ) {
                            setCode(activity.source);
                            setCompleted(false);
                        }
                    }}
                >
                    Reset
                </button>
                <button
                    onClick={() =>
                        download(activity.path.split("/").at(-1)!, code)
                    }
                >
                    Download ↓
                </button>
            </div>
            {completed && (
                <p className="pass" role="status">
                    ✓ All exercise cases passed for this saved draft.
                </p>
            )}
            {activity.support?.map((file) => (
                <details key={file.name}>
                    <summary>Read-only support file: {file.name}</summary>
                    <pre>{file.source}</pre>
                    <button onClick={() => download(file.name, file.source)}>
                        Download {file.name}
                    </button>
                </details>
            ))}
            <p className="execution-note">
                {activity.enabled
                    ? capability
                    : "Online execution is available for foundations only. Read, edit and download this activity."}
            </p>
            <label className="stdin-label">
                Standard input{" "}
                <span>One input per line, prepared before running.</span>
                <textarea
                    aria-label="Standard input"
                    value={stdin}
                    onChange={(e) => setStdin(e.target.value)}
                    placeholder="Enter the values your program will read…"
                    rows={4}
                />
            </label>
            <section className="results" aria-live="polite">
                <div className="results-title">
                    CONSOLE{" "}
                    <span>{result?.status ?? "Ready when you are"}</span>
                </div>
                {!result ? (
                    <p className="muted">
                        Your output and feedback will appear here.
                    </p>
                ) : (
                    <>
                        {result.message && <p>{result.message}</p>}
                        {result.compilation && <pre>{result.compilation}</pre>}
                        {result.cases?.map((c, i) => (
                            <details key={i} open={!c.passed}>
                                <summary className={c.passed ? "pass" : "fail"}>
                                    {c.passed ? "✓" : "×"} {c.name}
                                </summary>
                                {c.message && <p>{c.message}</p>}
                                <p>Input</p>
                                <pre>{c.input || "(none)"}</pre>
                                <p>Expected</p>
                                <pre>{c.expected}</pre>
                                <p>Output</p>
                                <pre>{c.stdout || "(empty)"}</pre>
                                {c.stderr && (
                                    <>
                                        <p>Errors</p>
                                        <pre>{c.stderr}</pre>
                                    </>
                                )}
                            </details>
                        ))}
                    </>
                )}
            </section>
            {activity.hints.length > 0 && (
                <section className="help">
                    <h3>A nudge in the right direction</h3>
                    <button
                        onClick={() => setHint(Math.min(3, hint + 1))}
                        disabled={hint === 3}
                    >
                        Reveal hint {Math.min(3, hint + 1)}
                    </button>
                    {activity.hints.slice(0, hint).map((text, i) => (
                        <pre key={i}>{text}</pre>
                    ))}
                    <details
                        onToggle={(event) => {
                            if (event.currentTarget.open && !solution)
                                void reveal();
                        }}
                    >
                        <summary>Review the reference solution</summary>
                        <p>
                            Try your own approach first. Compare the reasoning
                            as well as the result.
                        </p>
                        <pre>{solution || "Loading solution…"}</pre>
                    </details>
                </section>
            )}
        </>
    );
}
