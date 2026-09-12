import solutions from "@/generated/solutions.json";
export function GET(request: Request) {
    const id = new URL(request.url).searchParams.get("id") ?? "";
    const solution = (
        solutions as Record<string, { source: string; filename: string }>
    )[id];
    if (!solution)
        return Response.json({ message: "Not found" }, { status: 404 });
    return Response.json(solution, {
        headers: { "Cache-Control": "public, max-age=3600" },
    });
}
