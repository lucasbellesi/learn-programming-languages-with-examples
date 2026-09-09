import { auth } from "@/lib/server";
export async function GET(request: Request) {
    const url = new URL(request.url);
    const code = url.searchParams.get("code");
    const client = await auth();
    if (code && client) {
        const { error } = await client.auth.exchangeCodeForSession(code);
        if (!error)
            return new Response(null, {
                status: 303,
                headers: { Location: "/" },
            });
    }
    return new Response(null, {
        status: 303,
        headers: { Location: "/?auth=unavailable" },
    });
}
