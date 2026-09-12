import { executionConfigured, json } from "@/lib/server";
export const dynamic = "force-dynamic";
export function GET() {
    const execution = executionConfigured();
    return json({
        execution,
        message: execution
            ? "Free beta · guests: 5 runs/day · accounts: 25 runs/day. Shared capacity is limited."
            : "Online execution is temporarily unavailable. Editing and downloads remain available.",
    });
}
