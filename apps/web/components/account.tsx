"use client";
import { createBrowserClient } from "@supabase/ssr";
import { useEffect, useState } from "react";
import { allDrafts, saveDraft, type Draft } from "@/lib/browser-db";
export function Account() {
    const [name, setName] = useState<string>();
    const [message, setMessage] = useState("");
    const [conflicts, setConflicts] = useState<
        { local: Draft; remote: Draft }[]
    >([]);
    const configured = Boolean(
        process.env.NEXT_PUBLIC_SUPABASE_URL &&
        process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY,
    );
    useEffect(() => {
        if (configured)
            fetch("/api/account")
                .then((r) => r.json())
                .then((d) => setName(d.name))
                .catch(() => {});
    }, [configured]);
    useEffect(() => {
        if (name) void sync();
    }, [name]);
    async function login() {
        if (!configured) {
            setMessage(
                "Accounts are not configured yet. Your drafts stay on this device.",
            );
            return;
        }
        const client = createBrowserClient(
            process.env.NEXT_PUBLIC_SUPABASE_URL!,
            process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
        );
        const { error } = await client.auth.signInWithOAuth({
            provider: "github",
            options: { redirectTo: `${location.origin}/auth/callback` },
        });
        if (error)
            setMessage(
                "Sign-in is temporarily unavailable. Your local drafts are safe.",
            );
    }
    async function sync() {
        try {
            const response = await fetch("/api/drafts");
            if (!response.ok) throw Error();
            const remote: Draft[] = await response.json();
            const local = await allDrafts();
            const next = [];
            for (const draft of local) {
                const other = remote.find((d) => d.id === draft.id);
                if (other && other.code !== draft.code) {
                    next.push({ local: draft, remote: other });
                } else if (!other) {
                    await upload(draft);
                }
            }
            for (const draft of remote) {
                if (!local.some((d) => d.id === draft.id))
                    await saveDraft(draft);
            }
            setConflicts(next);
            setMessage(
                next.length
                    ? "Choose which draft to keep. Both copies are preserved until you choose."
                    : "Drafts synced. Reopen the exercise to load imported changes.",
            );
        } catch {
            setMessage("Sync is unavailable. Your local drafts are safe.");
        }
    }
    async function upload(
        draft: Draft,
        expectedUpdatedAt: string | null = null,
    ) {
        const response = await fetch("/api/drafts", {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ ...draft, expectedUpdatedAt }),
        });
        if (!response.ok) throw Error();
    }
    async function resolve(index: number, useLocal: boolean) {
        try {
            const pair = conflicts[index];
            const chosen = useLocal ? pair.local : pair.remote;
            if (useLocal) await upload(chosen, pair.remote.updatedAt);
            await saveDraft(chosen);
            setConflicts((current) => current.filter((_, i) => i !== index));
        } catch {
            setMessage("Could not save. Both drafts are still available.");
        }
    }
    async function logout() {
        const client = createBrowserClient(
            process.env.NEXT_PUBLIC_SUPABASE_URL!,
            process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
        );
        await client.auth.signOut();
        setName(undefined);
    }
    return (
        <div className="account">
            {name ? (
                <>
                    <button onClick={sync}>Sync drafts</button>
                    <button onClick={logout}>Sign out</button>
                </>
            ) : (
                <button className="account-button" onClick={login}>
                    Sign in with GitHub ↗
                </button>
            )}
            {message && (
                <div className="account-message" role="status">
                    <button
                        aria-label="Close account message"
                        onClick={() => setMessage("")}
                    >
                        ×
                    </button>
                    {message}
                    {conflicts.map((pair, i) => (
                        <div className="conflict" key={pair.local.id}>
                            <strong>{pair.local.id}</strong>
                            <details>
                                <summary>Compare copies</summary>
                                <p>This device</p>
                                <pre>{pair.local.code}</pre>
                                <p>Cloud</p>
                                <pre>{pair.remote.code}</pre>
                            </details>
                            <button onClick={() => resolve(i, true)}>
                                Keep this device
                            </button>
                            <button onClick={() => resolve(i, false)}>
                                Keep cloud
                            </button>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}
