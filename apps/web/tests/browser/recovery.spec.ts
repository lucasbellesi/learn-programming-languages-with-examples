import { readFile } from "node:fs/promises";
import { test, expect } from "@playwright/test";

const lesson = "/learn/python/01-foundations/types-and-io";
const draft = 'print("my downloadable draft")\n';

test("download contains the current draft and reset requires confirmation", async ({
    page,
}) => {
    await page.goto(lesson);
    await page.getByRole("tab", { name: "Exercise 01", exact: true }).click();
    const editor = page.getByRole("textbox", {
        name: "Code editor",
        exact: true,
    });
    await expect(page.locator(".monaco-editor")).toBeVisible();
    await editor.press("ControlOrMeta+A");
    await page.keyboard.type(draft);
    await expect(page.getByRole("status")).toHaveText("Saved on this device");
    const downloading = page.waitForEvent("download");
    await page.getByRole("button", { name: "Download ↓" }).click();
    const download = await downloading;
    expect(download.suggestedFilename()).toBe("01.py");
    expect(await readFile((await download.path())!, "utf8")).toBe(draft);

    page.once("dialog", (dialog) => dialog.dismiss());
    await page.getByRole("button", { name: "Reset", exact: true }).click();
    await expect(page.locator(".editor-shell")).toContainText(
        "my downloadable draft",
    );
    page.once("dialog", (dialog) => dialog.accept());
    await page.getByRole("button", { name: "Reset", exact: true }).click();
    await expect(page.locator(".editor-shell")).not.toContainText(
        "my downloadable draft",
    );
    await expect(page.locator(".editor-shell")).toContainText("TODO");
    await expect(page.getByRole("status")).toHaveText("Saved on this device");
    await page.reload();
    await page.getByRole("tab", { name: "Exercise 01", exact: true }).click();
    await expect(page.locator(".editor-shell")).toContainText("TODO");
    await expect(page.locator(".editor-shell")).not.toContainText(
        "my downloadable draft",
    );
});

test("reference solutions load without replacing the learner draft", async ({
    page,
}) => {
    await page.goto(lesson);
    await page.getByRole("tab", { name: "Exercise 01", exact: true }).click();
    const editor = page.getByRole("textbox", {
        name: "Code editor",
        exact: true,
    });
    await expect(page.locator(".monaco-editor")).toBeVisible();
    await editor.press("ControlOrMeta+A");
    await page.keyboard.type(draft);
    await page
        .getByText("Review the reference solution", { exact: true })
        .click();
    const solution = page
        .locator("details")
        .filter({ hasText: "Review the reference solution" })
        .locator("pre");
    await expect(solution).not.toHaveText("Loading solution…");
    await expect(solution).toContainText("print(");
    await expect(solution).not.toContainText("TODO");
    await expect(page.locator(".editor-shell")).toContainText(
        "my downloadable draft",
    );
});

test("an unavailable execution service leaves editing and downloading usable", async ({
    page,
}) => {
    await page.route("**/api/capabilities", (route) => route.abort());
    await page.goto(lesson);
    await expect(
        page.getByText(
            "Execution is unavailable. You can still edit and download.",
        ),
    ).toBeVisible();
    await expect(page.getByRole("button", { name: "Run code" })).toBeDisabled();
    const editor = page.getByRole("textbox", {
        name: "Code editor",
        exact: true,
    });
    await expect(page.locator(".monaco-editor")).toBeVisible();
    await editor.press("ControlOrMeta+A");
    await page.keyboard.type(draft);
    await expect(page.getByRole("status")).toHaveText("Saved on this device");
    const downloading = page.waitForEvent("download");
    await page.getByRole("button", { name: "Download ↓" }).click();
    expect(await readFile((await (await downloading).path())!, "utf8")).toBe(
        draft,
    );
});

test("quota errors show feedback and allow retrying without marking completion", async ({
    page,
}) => {
    await page.route("**/api/capabilities", (route) =>
        route.fulfill({ json: { execution: true, message: "Test mode" } }),
    );
    await page.route("**/api/executions", (route) =>
        route.fulfill({
            status: 429,
            json: { message: "Daily execution limit reached." },
        }),
    );
    await page.goto(lesson);
    await page.getByRole("tab", { name: "Exercise 01", exact: true }).click();
    const check = page.getByRole("button", { name: "Check exercise" });
    await check.click();
    await expect(page.locator(".results")).toContainText(
        "Daily execution limit reached.",
    );
    await expect(check).toBeEnabled();
    await expect(
        page.getByText("All exercise cases passed", { exact: false }),
    ).toHaveCount(0);
    await expect(
        page.getByRole("tab", { name: "Example", exact: true }),
    ).toBeEnabled();
});
