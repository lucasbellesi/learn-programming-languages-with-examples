import { randomBytes } from "node:crypto";
import { NextResponse, type NextRequest } from "next/server";

export function proxy(request: NextRequest) {
    const nonce = randomBytes(16).toString("base64");
    const development = process.env.NODE_ENV === "development";
    let provider = "";
    if (process.env.NEXT_PUBLIC_SUPABASE_URL) {
        try {
            const url = new URL(process.env.NEXT_PUBLIC_SUPABASE_URL);
            if (
                url.protocol === "https:" ||
                (development &&
                    url.protocol === "http:" &&
                    ["localhost", "127.0.0.1", "[::1]"].includes(url.hostname))
            )
                provider = url.origin;
        } catch {
            // An invalid optional account service must not break reading.
        }
    }
    const policy = [
        "default-src 'self'",
        `script-src 'self' 'nonce-${nonce}' 'strict-dynamic'${development ? " 'unsafe-eval'" : ""}`,
        // Monaco and the resizable workspace create dynamic inline styles.
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
        "worker-src 'self' blob:",
        `connect-src 'self' ${provider}${development ? " ws: wss:" : ""}`,
        "img-src 'self' data: blob:",
        "font-src 'self' data: https://fonts.gstatic.com",
        "object-src 'none'",
        "base-uri 'none'",
        "form-action 'self'",
        "frame-ancestors 'none'",
    ].join("; ");
    const headers = new Headers(request.headers);
    headers.set("x-nonce", nonce);
    headers.set("Content-Security-Policy", policy);
    const response = NextResponse.next({ request: { headers } });
    response.headers.set("Content-Security-Policy", policy);
    response.headers.set("Cache-Control", "private, no-store");
    return response;
}

export const config = {
    matcher: ["/((?!api/|_next/static|_next/image|monaco/|favicon.ico).*)"],
};
