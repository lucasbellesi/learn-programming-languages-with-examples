import { execFileSync } from "node:child_process";
import { cpSync, mkdirSync } from "node:fs";
if (
    process.env.VERCEL_ENV === "production" &&
    process.env.VERCEL_GIT_COMMIT_REF !== "master"
) {
    throw new Error(
        "Production builds are allowed only from master. Use a Preview deployment for this branch.",
    );
}
mkdirSync("public/monaco", { recursive: true });
cpSync("node_modules/monaco-editor/min/vs", "public/monaco/vs", {
    recursive: true,
});
execFileSync(
    process.platform === "win32" ? "python" : "python3",
    ["scripts/export-content.py"],
    { stdio: "inherit" },
);
