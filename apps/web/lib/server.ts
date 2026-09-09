import "server-only";
import { createServerClient } from "@supabase/ssr";
import { createClient } from "@supabase/supabase-js";
import { cookies } from "next/headers";
import { createHmac, randomUUID, timingSafeEqual } from "node:crypto";
export const accountConfigured = () =>
    Boolean(
        process.env.NEXT_PUBLIC_SUPABASE_URL &&
        process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY,
    );
export const executionConfigured = () =>
    Boolean(
        process.env.EXECUTION_ENABLED === "true" &&
        accountConfigured() &&
        process.env.SUPABASE_SERVICE_ROLE_KEY &&
        process.env.SESSION_SECRET &&
        process.env.SANDBOX_SNAPSHOT_ID,
    );
export function admin() {
    if (!process.env.SUPABASE_SERVICE_ROLE_KEY)
        throw Error("Service unavailable");
    return createClient(
        process.env.NEXT_PUBLIC_SUPABASE_URL!,
        process.env.SUPABASE_SERVICE_ROLE_KEY,
        { auth: { persistSession: false, autoRefreshToken: false } },
    );
}
export async function auth() {
    if (!accountConfigured()) return null;
    const jar = await cookies();
    return createServerClient(
        process.env.NEXT_PUBLIC_SUPABASE_URL!,
        process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
        {
            cookies: {
                getAll: () => jar.getAll(),
                setAll: (items) => {
                    for (const item of items)
                        jar.set(item.name, item.value, item.options);
                },
            },
        },
    );
}
export async function user() {
    const client = await auth();
    if (!client) return null;
    const {
        data: { user },
        error,
    } = await client.auth.getUser();
    if (error) return null;
    return user;
}
export function sameOrigin(request: Request) {
    const origin = request.headers.get("origin");
    // Next may use an internal hostname in request.url behind its proxy.
    // Host is the browser-requested authority; browser scripts cannot forge it.
    const host = request.headers.get("host");
    let valid = false;
    try {
        const parsed = new URL(origin ?? "");
        valid =
            parsed.origin === origin &&
            parsed.host === host &&
            (parsed.protocol === "https:" ||
                (process.env.NODE_ENV !== "production" &&
                    parsed.protocol === "http:"));
    } catch {
        /* A missing or malformed origin is rejected. */
    }
    if (!valid) throw Error("Invalid request origin");
}
export function digest(value: string) {
    return createHmac("sha256", process.env.SESSION_SECRET!)
        .update(value)
        .digest("hex");
}
export async function identity(request: Request) {
    const signedIn = await user();
    if (signedIn)
        return { id: `user:${signedIn.id}`, userId: signedIn.id, ip: null };
    if (!process.env.SESSION_SECRET) throw Error("Guest sessions unavailable");
    const jar = await cookies();
    const value = jar.get("learn_session")?.value;
    let id = "";
    if (value) {
        const [candidate, signature] = value.split(".");
        const expected = digest(candidate ?? "");
        if (
            signature?.length === expected.length &&
            timingSafeEqual(Buffer.from(signature), Buffer.from(expected)) &&
            /^[0-9a-f-]{36}$/.test(candidate)
        )
            id = candidate;
    }
    if (!id) {
        id = randomUUID();
        jar.set("learn_session", `${id}.${digest(id)}`, {
            httpOnly: true,
            sameSite: "lax",
            secure: process.env.NODE_ENV === "production",
            path: "/",
            maxAge: 60 * 60 * 24 * 30,
        });
    }
    const forwarded = request.headers.get("x-vercel-forwarded-for");
    const ip = process.env.VERCEL
        ? forwarded?.split(",")[0]?.trim()
        : "local-development";
    if (!ip) throw Error("Cannot verify guest network");
    return {
        id: `guest:${id}`,
        userId: null,
        ip: `ip:${digest(`${new Date().toISOString().slice(0, 10)}:${ip}`)}`,
    };
}
export function json(data: unknown, status = 200) {
    return Response.json(data, {
        status,
        headers: { "Cache-Control": "no-store" },
    });
}
