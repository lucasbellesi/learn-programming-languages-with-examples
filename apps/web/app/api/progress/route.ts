import { auth, json } from "@/lib/server";

export async function GET() {
    try {
        const client = await auth();
        if (!client)
            return json({ message: "Sign in to view verified progress." }, 401);
        const {
            data: { user },
            error: authError,
        } = await client.auth.getUser();
        if (authError || !user)
            return json({ message: "Sign in to view verified progress." }, 401);
        // Use the authenticated client, so RLS enforces ownership as well as this filter.
        const { data, error } = await client
            .from("progress")
            .select("activity_id, revision, verified_at")
            .eq("user_id", user.id);
        if (error) throw error;
        return json({ progress: data });
    } catch {
        return json(
            { message: "Verified progress is temporarily unavailable." },
            503,
        );
    }
}
