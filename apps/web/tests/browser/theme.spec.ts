import { test, expect } from "@playwright/test";

test("theme follows the system, persists an override, and can return to system", async ({
    page,
}) => {
    await page.emulateMedia({ colorScheme: "dark" });
    await page.goto("/");
    await expect(page.locator("html")).toHaveAttribute("data-theme", "dark");
    await expect(
        page.getByRole("button", { name: "Theme: System", exact: true }),
    ).toBeVisible();
    await page.emulateMedia({ colorScheme: "light" });
    await expect(page.locator("html")).toHaveAttribute("data-theme", "light");
    await page
        .getByRole("button", { name: "Theme: System", exact: true })
        .press("Enter");
    await expect(page.locator("html")).toHaveAttribute("data-theme", "dark");
    await page.reload();
    await expect(
        page.getByRole("button", { name: "Theme: Dark", exact: true }),
    ).toBeVisible();
    await expect(page.locator("html")).toHaveAttribute("data-theme", "dark");
    await page
        .getByRole("button", { name: "Theme: Dark", exact: true })
        .click();
    await page.emulateMedia({ colorScheme: "dark" });
    await expect(page.locator("html")).toHaveAttribute("data-theme", "light");
    await page
        .getByRole("button", { name: "Theme: Light", exact: true })
        .click();
    await expect(page.locator("html")).toHaveAttribute("data-theme", "dark");
    await page.setViewportSize({ width: 390, height: 844 });
    expect(
        await page.evaluate(
            () => document.documentElement.scrollWidth <= innerWidth,
        ),
    ).toBe(true);
});

test("theme changes update Monaco without replacing the draft", async ({
    page,
}) => {
    await page.emulateMedia({ colorScheme: "light" });
    await page.goto("/learn/python/01-foundations/types-and-io");
    const editor = page.getByRole("textbox", {
        name: "Code editor",
        exact: true,
    });
    await expect(editor).toBeVisible();
    await editor.press("ControlOrMeta+A");
    await page.keyboard.insertText('print("theme keeps my draft")\n');
    await page
        .getByRole("button", { name: "Theme: System", exact: true })
        .click();
    await expect(page.locator(".monaco-editor").first()).toHaveClass(/vs-dark/);
    await expect(page.locator(".editor-shell")).toContainText(
        "theme keeps my draft",
    );
    await page
        .getByRole("button", { name: "Theme: Dark", exact: true })
        .click();
    await expect(page.locator(".monaco-editor").first()).not.toHaveClass(
        /vs-dark/,
    );
    await expect(page.locator(".editor-shell")).toContainText(
        "theme keeps my draft",
    );
});

test("theme selection still works when local storage is unavailable", async ({
    page,
}) => {
    await page.addInitScript(() => {
        Storage.prototype.getItem = () => {
            throw Error("Storage unavailable");
        };
        Storage.prototype.setItem = () => {
            throw Error("Storage unavailable");
        };
        Storage.prototype.removeItem = () => {
            throw Error("Storage unavailable");
        };
    });
    await page.emulateMedia({ colorScheme: "dark" });
    await page.goto("/");
    await expect(page.locator("html")).toHaveAttribute("data-theme", "dark");
    await page
        .getByRole("button", { name: "Theme: System", exact: true })
        .click();
    await page
        .getByRole("button", { name: "Theme: Dark", exact: true })
        .click();
    await expect(page.locator("html")).toHaveAttribute("data-theme", "light");
});
