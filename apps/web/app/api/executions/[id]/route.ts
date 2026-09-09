import { admin, identity, json, sameOrigin } from "@/lib/server";
import { inspect } from "@/lib/executions";
export const maxDuration = 15;
async function handle(
    request: Request,
    params: Promise<{ id: string }>,
    cancel = false,
) {
    try {
        if (cancel) sameOrigin(request);
        const { id } = await params;
        if (!/^[0-9a-f-]{36}$/.test(id))
            return json({ message: "Not found" }, 404);
        const owner = await identity(request);
        const { data, error } = await admin()
            .from("executions")
            .select("*")
            .eq("id", id)
            .eq("identity", owner.id)
            .single();
        if (error || !data) return json({ message: "Not found" }, 404);
        return json(await inspect(data, cancel));
    } catch {
        return json(
            { message: "Execution status is temporarily unavailable" },
            503,
        );
    }
}
export async function GET(
    request: Request,
    { params }: { params: Promise<{ id: string }> },
) {
    return handle(request, params);
}
export async function DELETE(
    request: Request,
    { params }: { params: Promise<{ id: string }> },
) {
    return handle(request, params, true);
}
