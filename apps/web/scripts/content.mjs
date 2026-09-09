import { execFileSync } from "node:child_process";
import { cpSync, mkdirSync } from "node:fs";
mkdirSync("public/monaco", { recursive: true });
cpSync("node_modules/monaco-editor/min/vs", "public/monaco/vs", {
    recursive: true,
});
execFileSync(
    process.platform === "win32" ? "python" : "python3",
    ["scripts/export-content.py"],
    { stdio: "inherit" },
);
