import { json, user } from "@/lib/server";
export async function GET() {
    try {
        const current = await user();
        return json({
            name:
                current?.user_metadata?.user_name ??
                (current ? "Learner" : undefined),
        });
    } catch {
        return json({}, 503);
    }
}
