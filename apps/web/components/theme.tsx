"use client";

import { createContext, useContext, useEffect, useState } from "react";

type Preference = "system" | "light" | "dark";
const ThemeContext = createContext(false);
export const useDarkTheme = () => useContext(ThemeContext);
const key = "code-by-example-theme";
function readPreference(): Preference {
    try {
        const saved = localStorage.getItem(key);
        if (saved === "light" || saved === "dark") return saved;
    } catch {
        /* Theme selection also works without browser storage. */
    }
    return "system";
}

export function ThemeProvider({ children }: { children: React.ReactNode }) {
    const [preference, setPreference] = useState<Preference>("system");
    const [dark, setDark] = useState(false);
    useEffect(() => {
        const media = matchMedia("(prefers-color-scheme: dark)");
        const apply = (choice: Preference) => {
            const resolved =
                choice === "system" ? media.matches : choice === "dark";
            document.documentElement.dataset.theme = resolved
                ? "dark"
                : "light";
            setDark(resolved);
            setPreference(choice);
        };
        apply(readPreference());
        const systemChanged = () => {
            if (document.documentElement.dataset.themePreference === "system")
                apply("system");
        };
        const selected = (event: Event) =>
            apply((event as CustomEvent<Preference>).detail);
        const storageChanged = (event: StorageEvent) => {
            if (event.key === key || event.key === null) {
                const choice = readPreference();
                document.documentElement.dataset.themePreference = choice;
                apply(choice);
            }
        };
        document.documentElement.dataset.themePreference = readPreference();
        media.addEventListener("change", systemChanged);
        window.addEventListener("theme-choice", selected);
        window.addEventListener("storage", storageChanged);
        return () => {
            media.removeEventListener("change", systemChanged);
            window.removeEventListener("theme-choice", selected);
            window.removeEventListener("storage", storageChanged);
        };
    }, []);
    const next =
        preference === "system"
            ? "dark"
            : preference === "dark"
              ? "light"
              : "system";
    return (
        <ThemeContext.Provider value={dark}>
            <ThemeButtonContext.Provider value={{ preference, next }}>
                {children}
            </ThemeButtonContext.Provider>
        </ThemeContext.Provider>
    );
}

const ThemeButtonContext = createContext<{
    preference: Preference;
    next: Preference;
}>({ preference: "system", next: "dark" });
export function ThemeButton() {
    const { preference, next } = useContext(ThemeButtonContext);
    return (
        <button
            className="theme-button"
            title={`Switch to ${next} theme`}
            onClick={() => {
                try {
                    if (next === "system") localStorage.removeItem(key);
                    else localStorage.setItem(key, next);
                } catch {
                    /* Keep the choice for this page even when storage is unavailable. */
                }
                document.documentElement.dataset.themePreference = next;
                window.dispatchEvent(
                    new CustomEvent("theme-choice", { detail: next }),
                );
            }}
        >
            Theme: {preference[0].toUpperCase() + preference.slice(1)}
        </button>
    );
}
