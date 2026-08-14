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
    const original: Preferences = {
        theme: "light",
        shortcuts: ["save", "search"],
    };
    const clone = clonePreferences(original);

    clone.theme = "dark";
    clone.shortcuts.push("preview");

    console.log(`Original theme: ${original.theme}`);
    console.log(`Original shortcuts: ${original.shortcuts.join(", ")}`);
    console.log(`Clone theme: ${clone.theme}`);
    console.log(`Clone shortcuts: ${clone.shortcuts.join(", ")}`);
}

main();

export {};
