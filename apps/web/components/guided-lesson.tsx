"use client";
import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import type { Guide, Journey, Question } from "@/lib/guide-types";
import { journeyKey } from "@/lib/guide-types";
import {
    allDrafts,
    loadJourney,
    localActivityProgress,
    saveJourney,
    type ActivityProgress,
    type Draft,
} from "@/lib/browser-db";

function QuestionCard({
    question,
    answer,
    onAnswer,
}: {
    question: Question;
    answer?: string;
    onAnswer: (answer?: string) => void;
}) {
    const [choice, setChoice] = useState("");
    return (
        <fieldset className="question-card">
            <legend>{question.prompt}</legend>
            {question.options.map((option) => (
                <label key={option.id}>
                    <input
                        type="radio"
                        name={question.id}
                        value={option.id}
                        checked={(answer ?? choice) === option.id}
                        disabled={answer !== undefined}
                        onChange={() => setChoice(option.id)}
                    />
                    {option.text}
                </label>
            ))}
            {answer === undefined ? (
                <button disabled={!choice} onClick={() => onAnswer(choice)}>
                    Check answer
                </button>
            ) : (
                <>
                    <p role="status">
                        <strong>
                            {answer === question.correct
                                ? "Correct."
                                : "Not yet."}
                        </strong>{" "}
                        {question.explanation}
                    </p>
                    <button
                        onClick={() => {
                            setChoice("");
                            onAnswer();
                        }}
                    >
                        Try this question again
                    </button>
                </>
            )}
        </fieldset>
    );
}

export function GuidedLesson({
    guide,
    revision,
    openPractice,
}: {
    guide: Guide;
    revision: string;
    openPractice: (id: string, input?: string) => Promise<boolean>;
}) {
    const id = journeyKey(guide);
    const [journey, setJourney] = useState<Journey>({
        id,
        step: "understand",
        reviewed: [],
        answers: {},
        lastVisited: "",
    });
    const [ready, setReady] = useState(false);
    const [active, setActive] = useState(false);
    const [storageError, setStorageError] = useState("");
    const [notice, setNotice] = useState("");
    const [local, setLocal] = useState<ActivityProgress[]>([]);
    const [drafts, setDrafts] = useState<Draft[]>([]);
    const [verified, setVerified] = useState<
        { activity_id: string; revision: string; verified_at: string }[]
    >([]);
    const [remoteMessage, setRemoteMessage] = useState(
        "Sign in to view server-verified exercise history.",
    );
    const heading = useRef<HTMLHeadingElement>(null);
    const focusNext = useRef(false);
    const verifiedRequest = useRef(0);
    useEffect(() => {
        let live = true;
        loadJourney(id)
            .then((saved) => {
                if (live && saved) setJourney(saved);
            })
            .catch(() => {
                if (live)
                    setStorageError(
                        "Learning progress cannot be saved on this device. You can still use every step.",
                    );
            })
            .finally(() => {
                if (live) {
                    setReady(true);
                    if (location.hash === "#guided") setActive(true);
                }
            });
        const hashChanged = () => {
            if (location.hash === "#guided") {
                setActive(true);
                focusNext.current = true;
            }
        };
        window.addEventListener("hashchange", hashChanged);
        return () => {
            live = false;
            window.removeEventListener("hashchange", hashChanged);
        };
    }, [id]);
    useEffect(() => {
        if (!ready || !active) return;
        const snapshot = { ...journey, lastVisited: new Date().toISOString() };
        void saveJourney(snapshot).catch(() =>
            setStorageError(
                "Learning progress cannot be saved on this device. You can still use every step.",
            ),
        );
        if (focusNext.current) {
            heading.current?.focus();
            focusNext.current = false;
        }
    }, [journey, active, ready]);
    useEffect(() => {
        let live = true;
        const refresh = async () => {
            try {
                const [progress, saved] = await Promise.all([
                    localActivityProgress(),
                    allDrafts(),
                ]);
                if (live) {
                    setLocal(progress);
                    setDrafts(saved);
                }
            } catch {
                if (live)
                    setStorageError(
                        "Learning progress cannot be saved on this device. You can still use every step.",
                    );
            }
        };
        void refresh();
        window.addEventListener("learning-progress", refresh);
        return () => {
            live = false;
            window.removeEventListener("learning-progress", refresh);
        };
    }, []);
    async function refreshVerified() {
        const request = ++verifiedRequest.current;
        setVerified([]);
        try {
            const response = await fetch("/api/progress", {
                cache: "no-store",
            });
            if (request !== verifiedRequest.current) return;
            if (response.status === 401) {
                setRemoteMessage(
                    "Sign in to view server-verified exercise history.",
                );
                return;
            }
            if (!response.ok) throw Error();
            const result = await response.json();
            if (request !== verifiedRequest.current) return;
            setVerified(result.progress);
            setRemoteMessage(
                "Server-verified history belongs to the signed-in account. It does not approve your current edited draft.",
            );
        } catch {
            if (request !== verifiedRequest.current) return;
            setRemoteMessage(
                "Server-verified history is unavailable. Local learning is still available.",
            );
        }
    }
    useEffect(() => {
        void refreshVerified();
        const clearAccount = () => {
            setVerified([]);
            void refreshVerified();
        };
        window.addEventListener("learning-account", clearAccount);
        return () => {
            verifiedRequest.current++;
            window.removeEventListener("learning-account", clearAccount);
        };
    }, []);
    function answer(question: string, value?: string) {
        setJourney((current) => {
            const answers = { ...current.answers };
            if (value === undefined) delete answers[question];
            else answers[question] = value;
            return { ...current, answers };
        });
    }
    async function open(id: string, input?: string) {
        if (!(await openPractice(id, input)))
            setNotice(
                "The editor could not be opened. Wait for loading or execution to finish, or keep your current input if you cancelled the replacement.",
            );
        else setNotice("");
    }
    const step =
        guide.steps.find((s) => s.id === journey.step) ?? guide.steps[0];
    const answered = guide.review.filter(
        (q) => journey.answers[q.id] !== undefined,
    ).length;
    const correct = guide.review.filter(
        (q) => journey.answers[q.id] === q.correct,
    ).length;
    return (
        <section
            className="guided-lesson"
            id="guided"
            aria-label="Guided lesson"
        >
            <div className="guide-intro">
                <div>
                    <span className="eyebrow">OPTIONAL · BEGINNER PATH</span>
                    <h2>One concept, six small steps.</h2>
                    <p>
                        Move freely between steps. Your guide stays on this
                        device.
                    </p>
                </div>
                <button
                    disabled={!ready}
                    onClick={() => {
                        focusNext.current = true;
                        setActive((value) => !value);
                        setJourney((current) => ({
                            ...current,
                            lastVisited: new Date().toISOString(),
                        }));
                    }}
                >
                    {active
                        ? "Hide guided lesson"
                        : journey.lastVisited
                          ? "Continue learning"
                          : "Start guided lesson"}
                </button>
            </div>
            {storageError && (
                <div role="alert">
                    <p>{storageError}</p>
                    <p>
                        If an older tab is open, close it and reload to restore
                        local saving.
                    </p>
                </div>
            )}
            {active && ready && (
                <>
                    <nav className="guide-steps" aria-label="Learning steps">
                        {guide.steps.map((s) => (
                            <button
                                key={s.id}
                                aria-current={
                                    step.id === s.id ? "step" : undefined
                                }
                                onClick={() => {
                                    focusNext.current = true;
                                    setJourney((current) => ({
                                        ...current,
                                        step: s.id,
                                    }));
                                }}
                            >
                                {s.title}
                                {journey.reviewed.includes(s.id) ? " ✓" : ""}
                            </button>
                        ))}
                    </nav>
                    <h3 ref={heading} tabIndex={-1}>
                        {step.title}
                    </h3>
                    <p>{step.text}</p>
                    {step.id === "understand" && (
                        <pre>{guide.fragments.join("\n")}</pre>
                    )}
                    {step.id === "predict" && (
                        <QuestionCard
                            key={guide.prediction.id}
                            question={guide.prediction}
                            answer={journey.answers[guide.prediction.id]}
                            onAnswer={(value) =>
                                answer(guide.prediction.id, value)
                            }
                        />
                    )}
                    {(step.id === "run" || step.id === "modify") && (
                        <>
                            {step.id === "run" && (
                                <p>
                                    Your recorded prediction:{" "}
                                    {guide.prediction.options.find(
                                        (o) =>
                                            o.id ===
                                            journey.answers[
                                                guide.prediction.id
                                            ],
                                    )?.text ??
                                        "No prediction yet — you can return to Predict at any time."}
                                </p>
                            )}
                            <div className="guide-actions">
                                <button onClick={() => open(guide.exampleId)}>
                                    Open example in editor
                                </button>
                                <button
                                    onClick={() =>
                                        open(
                                            guide.exampleId,
                                            guide.preparedInput,
                                        )
                                    }
                                >
                                    Load guided inputs into example
                                </button>
                            </div>
                            <p>
                                Prepared inputs: Ada Lovelace, 17, 3.5 — one
                                value per line. Use Run code in the editor when
                                execution is available.
                            </p>
                            <details>
                                <summary>
                                    Show reference output (not an execution)
                                </summary>
                                <p>
                                    For the original example and the prepared
                                    inputs. Prompts and the summary heading are
                                    omitted. This does not count as a run or a
                                    passed exercise.
                                </p>
                                <pre>{guide.referenceOutput}</pre>
                            </details>
                        </>
                    )}
                    {step.id === "solve" && (
                        <div className="guide-actions">
                            {guide.exerciseIds.map((activity, index) => (
                                <button
                                    key={activity}
                                    onClick={() => open(activity)}
                                >
                                    Open Exercise 0{index + 1}
                                </button>
                            ))}
                        </div>
                    )}
                    {step.id === "review" && (
                        <>
                            {guide.review.map((q) => (
                                <QuestionCard
                                    key={
                                        q.id +
                                        (journey.answers[q.id] === undefined
                                            ? "new"
                                            : "answered")
                                    }
                                    question={q}
                                    answer={journey.answers[q.id]}
                                    onAnswer={(value) => answer(q.id, value)}
                                />
                            ))}
                            <p aria-live="polite">
                                Review: {answered} of 3 answered · {correct} of
                                3 correct. These answers do not approve coding
                                exercises.
                            </p>
                            <button
                                onClick={() =>
                                    setJourney((current) => ({
                                        ...current,
                                        answers: Object.fromEntries(
                                            Object.entries(
                                                current.answers,
                                            ).filter(
                                                ([key]) =>
                                                    !guide.review.some(
                                                        (q) => q.id === key,
                                                    ),
                                            ),
                                        ),
                                    }))
                                }
                            >
                                Repeat review questions
                            </button>
                            <p>
                                <Link href={`/learn/${guide.nextModuleId}`}>
                                    Next: Operators and Expressions →
                                </Link>{" "}
                                — this module currently uses the regular reading
                                and practice experience.
                            </p>
                        </>
                    )}
                    <p>
                        <button
                            disabled={journey.reviewed.includes(step.id)}
                            onClick={() =>
                                setJourney((current) => ({
                                    ...current,
                                    reviewed: [
                                        ...new Set([
                                            ...current.reviewed,
                                            step.id,
                                        ]),
                                    ],
                                }))
                            }
                        >
                            {journey.reviewed.includes(step.id)
                                ? "Step reviewed"
                                : "Mark this step reviewed"}
                        </button>
                    </p>
                    {notice && <p role="alert">{notice}</p>}
                    <details className="guide-progress">
                        <summary>Your exercise progress</summary>
                        <p>
                            Visited and Attempted describe activity on this
                            device. Questions and reference solutions never
                            approve an exercise.
                        </p>
                        {guide.exerciseIds.map((activity, i) => {
                            const progress = local.find(
                                (p) => p.id === activity,
                            );
                            const draft = drafts.find((d) => d.id === activity);
                            const currentPassed = Boolean(
                                progress?.passedAt &&
                                draft?.passed &&
                                draft.revision === revision,
                            );
                            return (
                                <p key={activity}>
                                    Exercise 0{i + 1}:{" "}
                                    {currentPassed
                                        ? "Passed on this device"
                                        : progress?.attemptedAt
                                          ? "Attempted"
                                          : progress?.visitedAt
                                            ? "Visited"
                                            : "Not visited"}
                                    {progress?.passedAt && !currentPassed
                                        ? " · Historical pass on this device; current draft is not approved."
                                        : ""}
                                </p>
                            );
                        })}
                        <h4>Server-verified history</h4>
                        <p>{remoteMessage}</p>
                        {verified
                            .filter((p) =>
                                guide.exerciseIds.includes(p.activity_id),
                            )
                            .map((p) => (
                                <p key={p.activity_id + p.revision}>
                                    Exercise {p.activity_id.split("/").at(-1)} ·
                                    verified{" "}
                                    {new Date(
                                        p.verified_at,
                                    ).toLocaleDateString()}{" "}
                                    ·{" "}
                                    {p.revision === revision
                                        ? "current content revision"
                                        : "earlier content revision"}
                                </p>
                            ))}
                        <button onClick={refreshVerified}>
                            Refresh verified history
                        </button>
                    </details>
                </>
            )}
        </section>
    );
}

export function GuideEntry({
    guide,
}: {
    guide: Pick<Guide, "moduleId" | "version">;
}) {
    const [continued, setContinued] = useState(false);
    useEffect(() => {
        void loadJourney(journeyKey(guide))
            .then((value) => setContinued(Boolean(value?.lastVisited)))
            .catch(() => {});
    }, [guide.moduleId, guide.version]);
    return (
        <Link className="guide-entry" href={`/learn/${guide.moduleId}#guided`}>
            {continued ? "Continue learning" : "Start guided lesson"} →
        </Link>
    );
}
