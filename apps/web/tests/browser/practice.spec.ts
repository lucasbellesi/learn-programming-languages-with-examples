import { test, expect } from "@playwright/test";

test("failed storage warns before leaving and still allows downloads", async ({
    page,
}) => {
    await page.addInitScript(() => {
        indexedDB.open = () => {
            throw new Error("Storage disabled for this test");
        };
    });
    await page.goto("/learn/python/01-foundations/types-and-io");
    const editor = page.getByRole("textbox", {
        name: "Code editor",
        exact: true,
    });
    await expect(editor).toBeVisible();
    await editor.press("ControlOrMeta+A");
    await page.keyboard.insertText('print("keep these unsaved edits")\n');
    await expect(page.getByRole("status")).toHaveText(
        "Could not save. Download your code.",
    );
    let warnings = 0;
    page.on("dialog", async (dialog) => {
        warnings++;
        await dialog.dismiss();
    });
    await page.getByRole("link", { name: "← Back to the curriculum" }).click();
    await expect(page).toHaveURL(/python\/01-foundations\/types-and-io$/);
    await expect.poll(() => warnings).toBe(1);
    const downloaded = page.waitForEvent("download");
    await page.getByRole("button", { name: "Download ↓" }).click();
    expect((await downloaded).suggestedFilename()).toBe("main.py");
    expect(warnings).toBe(1);
});

test("mobile reading and practice preserve edits when switching panels", async ({
    page,
}) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/learn/python/01-foundations/types-and-io");
    await expect(page.locator("article.reading")).toBeVisible();
    await expect(
        page.getByRole("region", { name: "Code practice" }),
    ).toBeHidden();
    await page.getByRole("button", { name: "Practice", exact: true }).click();
    await page.getByRole("tab", { name: "Exercise 01", exact: true }).click();
    const editor = page.getByRole("textbox", {
        name: "Code editor",
        exact: true,
    });
    await expect(editor).toBeVisible();
    await editor.press("ControlOrMeta+A");
    await page.keyboard.insertText('print("mobile draft")\n');
    await expect(page.getByRole("status")).toHaveText("Saved on this device");
    await page.getByRole("button", { name: "Read", exact: true }).click();
    await expect(page.locator("article.reading")).toBeVisible();
    await page.getByRole("button", { name: "Practice", exact: true }).click();
    await expect(page.locator(".editor-shell")).toContainText("mobile draft");
    expect(
        await page.evaluate(
            () => document.documentElement.scrollWidth <= window.innerWidth,
        ),
    ).toBe(true);
});

test("language navigation preserves the concept", async ({ page }) => {
    await page.goto("/learn/python/01-foundations/types-and-io");
    await page
        .getByLabel("Language for this concept")
        .selectOption("typescript");
    await expect(page).toHaveURL(/typescript\/01-foundations\/types-and-io$/);
    await expect(page.getByLabel("Language for this concept")).toHaveValue(
        "typescript",
    );
    await expect(page.getByRole("heading", { level: 1 })).toContainText(
        "Types and Input/Output",
    );
});

test("draft survives reload while execution is disabled", async ({ page }) => {
    await page.goto("/learn/python/01-foundations/types-and-io");
    await page.getByRole("tab", { name: "Exercise 01", exact: true }).click();
    const editor = page.getByRole("textbox", {
        name: "Code editor",
        exact: true,
    });
    await expect(editor).toBeVisible();
    await editor.press("ControlOrMeta+A");
    await page.keyboard.insertText('print("saved browser draft")\n');
    await expect(page.getByRole("status")).toHaveText("Saved on this device");
    await page.reload();
    await page.getByRole("tab", { name: "Exercise 01", exact: true }).click();
    await expect(page.locator(".editor-shell")).toContainText(
        "saved browser draft",
    );
    await expect(
        page.getByRole("button", { name: "Check exercise" }),
    ).toBeDisabled();
    await page.getByRole("button", { name: "Reveal hint 1" }).click();
    await expect(
        page.getByRole("button", { name: "Reveal hint 2" }),
    ).toBeVisible();
});

test("execution feedback is rendered and completion follows the saved code", async ({
    page,
}) => {
    // Cloud integration is tested separately against Sandbox and Supabase.
    // This test makes no cloud requests and is safe for untrusted PR CI.
    await page.route("**/api/capabilities", (route) =>
        route.fulfill({ json: { execution: true, message: "Test mode" } }),
    );
    await page.route("**/api/executions", (route) =>
        route.fulfill({
            status: 202,
            json: { id: "test-job", status: "running" },
        }),
    );
    await page.route("**/api/executions/test-job", (route) =>
        route.fulfill({
            json: {
                id: "test-job",
                status: "passed",
                cases: [
                    {
                        name: "Normal case",
                        input: "3",
                        expected: "6",
                        stdout: "6",
                        stderr: "",
                        passed: true,
                    },
                ],
            },
        }),
    );
    await page.goto("/learn/python/01-foundations/types-and-io");
    await page.getByRole("tab", { name: "Exercise 01", exact: true }).click();
    await page.getByRole("button", { name: "Check exercise" }).click();
    await expect(
        page.getByText("All exercise cases passed for this saved draft.", {
            exact: false,
        }),
    ).toBeVisible();
    await page.getByText("✓ Normal case", { exact: true }).click();
    await expect(
        page.locator("details").filter({ hasText: "Normal case" }),
    ).toContainText("6");
});
