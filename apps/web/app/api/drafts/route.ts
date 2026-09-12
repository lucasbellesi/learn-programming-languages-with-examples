import { z } from "zod";
import { auth, json, sameOrigin, user } from "@/lib/server";
import { catalog } from "@/lib/catalog";
const schema = z.object({
    id: z.string().max(200),
    code: z.string().refine((v) => Buffer.byteLength(v) <= 65536),
    revision: z.string().regex(/^[a-f0-9]{40}$/),
    passed: z.boolean().optional(),
    expectedUpdatedAt: z.string().datetime({ offset: true }).nullable(),
});
export async function GET() {
    try {
        const current = await user();
        if (!current) return json({ message: "Sign in to sync" }, 401);
        const client = (await auth())!;
        const { data, error } = await client
            .from("drafts")
            .select("activity_id,code,revision,updated_at,imported_passed")
            .eq("user_id", current.id);
        if (error) throw error;
        return json(
            data.map((d) => ({
                id: d.activity_id,
                code: d.code,
                revision: d.revision,
                updatedAt: d.updated_at,
                passed: d.imported_passed,
            })),
        );
    } catch {
        return json({ message: "Sync unavailable" }, 503);
    }
}
export async function PUT(request: Request) {
    try {
        sameOrigin(request);
        const current = await user();
        if (!current) return json({ message: "Sign in to sync" }, 401);
        const text = await request.text();
        if (Buffer.byteLength(text) > 80000)
            return json({ message: "Draft too large" }, 413);
        const draft = schema.parse(JSON.parse(text));
        if (!catalog.activities[draft.id])
            return json({ message: "Unknown activity" }, 400);
        const client = (await auth())!;
        const record = {
            user_id: current.id,
            activity_id: draft.id,
            code: draft.code,
            revision: draft.revision,
            updated_at: new Date().toISOString(),
            imported_passed: draft.passed ?? false,
        };
        const mutation =
            draft.expectedUpdatedAt === null
                ? client.from("drafts").insert(record)
                : client
                      .from("drafts")
                      .update(record)
                      .eq("user_id", current.id)
                      .eq("activity_id", draft.id)
                      .eq("updated_at", draft.expectedUpdatedAt);
        const { data: changed, error } = await mutation.select("updated_at");
        if (error?.code === "23505" || (!error && !changed?.length))
            return json(
                {
                    message:
                        "The cloud draft changed. Sync again before choosing a copy.",
                },
                409,
            );
        if (error) throw error;
        return json({ saved: true, updatedAt: record.updated_at });
    } catch {
        return json({ message: "Draft could not be saved" }, 400);
    }
}
