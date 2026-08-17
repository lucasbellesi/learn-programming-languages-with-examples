import { readFileSync } from "node:fs";

type Preferences = {
    theme: string;
    shortcuts: string[];
};

function clonePreferences(source: Preferences): Preferences {
    return {
        theme: source.theme,
        shortcuts: [...source.shortcuts],
    };
}

function main(): void {
    const [
        originalTheme = "light",
        shortcutLine = "",
        cloneTheme = "dark",
        added = "",
    ] = readFileSync(0, "utf8").trimEnd().split(/\r?\n/);
    const original: Preferences = {
        theme: originalTheme,
        shortcuts: shortcutLine
            .split(",")
            .map((shortcut) => shortcut.trim())
            .filter((shortcut) => shortcut.length > 0),
    };
    const clone = clonePreferences(original);

    clone.theme = cloneTheme;
    if (added.trim().length > 0) {
        clone.shortcuts.push(added.trim());
    }

    console.log(`Original theme: ${original.theme}`);
    console.log(
        `Original shortcuts: ${original.shortcuts.join(", ") || "none"}`,
    );
    console.log(`Clone theme: ${clone.theme}`);
    console.log(`Clone shortcuts: ${clone.shortcuts.join(", ") || "none"}`);
}

main();

export {};
