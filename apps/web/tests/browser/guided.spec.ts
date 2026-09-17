import { test, expect } from "@playwright/test";
import type { Route } from "@playwright/test";

const moduleId = "python/01-foundations/types-and-io";
const route = `/learn/${moduleId}#guided`;

test("an older open tab cannot leave the storage upgrade hanging", async ({
    page,
    context,
}) => {
    const older = await context.newPage();
    await older.goto("/api/capabilities");
    await older.evaluate(
        () =>
            new Promise<void>((resolve) => {
                const request = indexedDB.open("programming-examples", 1);
                request.onupgradeneeded = () =>
                    request.result.createObjectStore("drafts", {
                        keyPath: "id",
                    });
                request.onsuccess = () => {
                    (window as unknown as { legacyDb: IDBDatabase }).legacyDb =
                        request.result;
                    resolve();
                };
            }),
    );
    await page.goto(route);
    await expect(
        page.getByText(
            "If an older tab is open, close it and reload to restore local saving.",
        ),
    ).toBeVisible();
    await step(page, "Review").click();
    await expect(page.locator(".question-card")).toHaveCount(3);
    await older.close();
    await page.reload();
    await expect(
        page.getByRole("button", { name: "Hide guided lesson" }),
    ).toBeVisible();
    await expect(
        page.getByText(
            "If an older tab is open, close it and reload to restore local saving.",
        ),
    ).toHaveCount(0);
});

test("late history responses cannot restore the previous account after sign-out", async ({
    page,
}) => {
    const pending: Route[] = [];
    let signedOut = false;
    let requests = 0;
    await page.route("**/api/progress", (route) => {
        requests++;
        if (!signedOut) {
            pending.push(route);
            return;
        }
        return route.fulfill({ status: 401, json: { message: "Sign in" } });
    });
    await page.goto(route);
    await expect.poll(() => pending.length).toBeGreaterThan(0);
    const beforeSignOut = requests;
    signedOut = true;
    await page.evaluate(() =>
        window.dispatchEvent(new Event("learning-account")),
    );
    await expect.poll(() => requests).toBeGreaterThan(beforeSignOut);
    for (const oldRequest of pending)
        await oldRequest.fulfill({
            json: {
                progress: [
                    {
                        activity_id: moduleId + "/02",
                        revision: "previous-user",
                        verified_at: "2026-09-01T00:00:00Z",
                    },
                ],
            },
        });
    await page.getByText("Your exercise progress", { exact: true }).click();
    await expect(
        page.getByText("Sign in to view server-verified exercise history."),
    ).toBeVisible();
    await expect(page.getByText(/Exercise 02 · verified/)).toHaveCount(0);
});
const step = (page: import("@playwright/test").Page, name: string) =>
    page
        .getByRole("navigation", { name: "Learning steps" })
        .getByRole("button", { name, exact: true });

test("prediction, review and resume work without using execution quota", async ({
    page,
}) => {
    let executions = 0;
    page.on("request", (request) => {
        if (request.url().endsWith("/api/executions")) executions++;
    });
    await page.goto("/");
    await page
        .getByRole("link", { name: "Start guided lesson →", exact: true })
        .click();
    await expect(
        page.getByRole("heading", { name: "Understand", exact: true }),
    ).toBeVisible();
    await step(page, "Predict").click();
    await expect(
        page.getByRole("heading", { name: "Predict", exact: true }),
    ).toBeFocused();
    await expect(page.getByText(/Seventeen is less than eighteen/)).toHaveCount(
        0,
    );
    await page.getByRole("radio", { name: "Adult: True", exact: true }).check();
    await page
        .getByRole("button", { name: "Check answer", exact: true })
        .click();
    await expect(page.getByText(/Not yet./)).toBeVisible();
    await page.reload();
    await expect(
        page.getByRole("heading", { name: "Predict", exact: true }),
    ).toBeVisible();
    await expect(
        page.getByRole("radio", { name: "Adult: True", exact: true }),
    ).toBeChecked();
    await page.getByRole("button", { name: "Try this question again" }).click();
    await expect(page.getByText(/Seventeen is less than eighteen/)).toHaveCount(
        0,
    );
    await page
        .getByRole("radio", { name: "Adult: False", exact: true })
        .check();
    await page
        .getByRole("button", { name: "Check answer", exact: true })
        .click();
    await expect(page.getByText(/Correct./).first()).toBeVisible();
    await step(page, "Review").click();
    for (const [index, answer] of [
        "str",
        'int("Ada")',
        "To avoid division by zero and an empty collection with no minimum or maximum.",
    ].entries()) {
        const question = page.locator(".question-card").nth(index);
        await question
            .getByRole("radio", { name: answer, exact: true })
            .check();
        await question.getByRole("button", { name: "Check answer" }).click();
    }
    await expect(
        page.getByText("Review: 3 of 3 answered · 3 of 3 correct.", {
            exact: false,
        }),
    ).toBeVisible();
    await page.getByText("Your exercise progress", { exact: true }).click();
    await expect(
        page.getByText("Exercise 01: Not visited", { exact: true }),
    ).toBeVisible();
    await page.getByRole("button", { name: "Repeat review questions" }).click();
    await expect(
        page.getByText("Review: 0 of 3 answered", { exact: false }),
    ).toBeVisible();
    expect(executions).toBe(0);
    await page.goto("/");
    await expect(
        page.getByRole("link", { name: "Continue learning →", exact: true }),
    ).toBeVisible();
});

test("guide preserves drafts, requires input replacement confirmation and remains usable on mobile", async ({
    page,
}) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.emulateMedia({ colorScheme: "dark" });
    await page.goto(route);
    await step(page, "Run").click();
    await page
        .getByRole("button", { name: "Open example in editor", exact: true })
        .click();
    const editor = page.getByRole("textbox", {
        name: "Code editor",
        exact: true,
    });
    await expect(editor).toBeVisible();
    await editor.press("ControlOrMeta+A");
    await page.keyboard.insertText('print("keep my own code")\n');
    await page
        .getByRole("textbox", { name: "Standard input", exact: true })
        .fill("my input");
    page.once("dialog", (dialog) => dialog.dismiss());
    await page
        .getByRole("button", { name: "Load guided inputs into example" })
        .click();
    await expect(
        page.getByRole("textbox", { name: "Standard input", exact: true }),
    ).toHaveValue("my input");
    page.once("dialog", (dialog) => dialog.accept());
    await page
        .getByRole("button", { name: "Load guided inputs into example" })
        .click();
    await expect(
        page.getByRole("textbox", { name: "Standard input", exact: true }),
    ).toHaveValue("Ada Lovelace\n17\n3.5");
    await expect(page.locator(".editor-shell")).toContainText(
        "keep my own code",
    );
    await step(page, "Modify").click();
    await expect(
        page.getByRole("heading", { name: "Modify", exact: true }),
    ).toBeFocused();
    await page
        .getByText("Show reference output (not an execution)", { exact: true })
        .click();
    await expect(
        page.getByText(/This does not count as a run or a passed exercise/),
    ).toBeVisible();
    await expect(
        page.getByRole("button", { name: "▶ Run code", exact: true }),
    ).toBeDisabled();
    expect(
        await page.evaluate(
            () => document.documentElement.scrollWidth <= innerWidth,
        ),
    ).toBe(true);
});

test("version-one database upgrades preserve drafts and old journey versions do not count as new answers", async ({
    page,
}) => {
    await page.goto("/api/capabilities");
    await page.evaluate(async (id) => {
        await new Promise<void>((resolve, reject) => {
            const request = indexedDB.open("programming-examples", 1);
            request.onupgradeneeded = () =>
                request.result.createObjectStore("drafts", { keyPath: "id" });
            request.onerror = () => reject(request.error);
            request.onsuccess = () => {
                const db = request.result;
                const tx = db.transaction("drafts", "readwrite");
                tx.objectStore("drafts").put({
                    id: id + "/example",
                    code: 'print("legacy draft")',
                    revision: "old-git-sha",
                    updatedAt: new Date().toISOString(),
                });
                tx.oncomplete = () => {
                    db.close();
                    resolve();
                };
            };
        });
    }, moduleId);
    await page.goto(route);
    await expect(page.locator(".editor-shell")).toContainText("legacy draft");
    await step(page, "Solve").click();
    await expect
        .poll(async () =>
            page.evaluate(async (id) => {
                return new Promise<string>((resolve) => {
                    const request = indexedDB.open("programming-examples", 2);
                    request.onsuccess = () => {
                        const db = request.result;
                        const get = db
                            .transaction("journeys")
                            .objectStore("journeys")
                            .get(id + "@1");
                        get.onsuccess = () => {
                            db.close();
                            resolve(get.result?.step ?? "");
                        };
                    };
                });
            }, moduleId),
        )
        .toBe("solve");
    await page.evaluate(async (id) => {
        await new Promise<void>((resolve) => {
            const request = indexedDB.open("programming-examples", 2);
            request.onsuccess = () => {
                const db = request.result;
                const tx = db.transaction("journeys", "readwrite");
                tx.objectStore("journeys").delete(id + "@1");
                tx.objectStore("journeys").put({
                    id: id + "@0",
                    step: "review",
                    answers: { "adult-17": "1" },
                    reviewed: ["understand"],
                    lastVisited: new Date().toISOString(),
                });
                tx.oncomplete = () => {
                    db.close();
                    resolve();
                };
            };
        });
    }, moduleId);
    await page.reload();
    await expect(
        page.getByRole("heading", { name: "Understand", exact: true }),
    ).toBeVisible();
    await step(page, "Predict").click();
    await expect(
        page.getByRole("button", { name: "Check answer", exact: true }),
    ).toBeDisabled();
    await expect(page.locator(".editor-shell")).toContainText("legacy draft");
});

test("storage failure does not block the guide and progress endpoint is read-only and authenticated", async ({
    page,
    request,
}) => {
    expect((await request.get("/api/progress")).status()).toBe(401);
    expect(
        (
            await request.post("/api/progress", { data: { passed: true } })
        ).status(),
    ).toBe(405);
    await page.addInitScript(() => {
        indexedDB.open = () => {
            throw Error("blocked storage");
        };
    });
    await page.goto(route);
    await expect(
        page.getByText(
            "Learning progress cannot be saved on this device. You can still use every step.",
        ),
    ).toBeVisible();
    await step(page, "Review").click();
    const first = page.locator(".question-card").first();
    await first.getByRole("radio", { name: "str", exact: true }).check();
    await first.getByRole("button", { name: "Check answer" }).click();
    await expect(first.getByText(/Correct./)).toBeVisible();
});

test("failed checks show targeted feedback and quota exhaustion permits review", async ({
    page,
}) => {
    await page.route("**/api/capabilities", (route) =>
        route.fulfill({ json: { execution: true, message: "Test mode" } }),
    );
    let attempts = 0;
    await page.route("**/api/executions", (route) => {
        attempts++;
        return attempts === 1
            ? route.fulfill({
                  json: {
                      status: "failed",
                      cases: [
                          {
                              name: "edge: N <= 0",
                              passed: false,
                              input: "0",
                              expected: "Please enter a positive count.",
                              stdout: "",
                              stderr: "",
                              message: "Output did not match",
                          },
                      ],
                  },
              })
            : route.fulfill({
                  status: 429,
                  json: { message: "Daily execution limit reached" },
              });
    });
    await page.goto(route);
    await step(page, "Solve").click();
    await page
        .getByRole("button", { name: "Open Exercise 01", exact: true })
        .click();
    await page
        .getByRole("button", { name: "Check exercise", exact: true })
        .click();
    await expect(
        page.getByText(
            "Reject non-positive counts before calculating a summary.",
        ),
    ).toBeVisible();
    await expect(
        page.getByText("For more guidance, use hint 2 below."),
    ).toBeVisible();
    await page
        .getByRole("button", { name: "Check exercise", exact: true })
        .click();
    await expect(
        page.getByText("Daily execution limit reached", { exact: true }),
    ).toBeVisible();
    await step(page, "Review").click();
    await expect(page.locator(".question-card")).toHaveCount(3);
    await page.getByText("Your exercise progress", { exact: true }).click();
    await expect(
        page.getByText("Exercise 01: Attempted", { exact: true }),
    ).toBeVisible();
});

test("editing removes current approval but retains local and separately verified history", async ({
    page,
}) => {
    await page.route("**/api/capabilities", (route) =>
        route.fulfill({ json: { execution: true, message: "Test mode" } }),
    );
    await page.route("**/api/executions", (route) =>
        route.fulfill({ json: { status: "passed", cases: [] } }),
    );
    await page.route("**/api/progress", (route) =>
        route.fulfill({
            json: {
                progress: [
                    {
                        activity_id: moduleId + "/02",
                        revision: "older-revision",
                        verified_at: "2026-09-01T00:00:00Z",
                    },
                ],
            },
        }),
    );
    await page.goto(route);
    await step(page, "Solve").click();
    await page
        .getByRole("button", { name: "Open Exercise 01", exact: true })
        .click();
    await page
        .getByRole("button", { name: "Check exercise", exact: true })
        .click();
    await page.getByText("Your exercise progress", { exact: true }).click();
    await expect(
        page.getByText("Exercise 01: Passed on this device", { exact: true }),
    ).toBeVisible();
    await expect(page.getByText(/Exercise 02 · verified/)).toBeVisible();
    const editor = page.getByRole("textbox", {
        name: "Code editor",
        exact: true,
    });
    await editor.press("ControlOrMeta+A");
    await page.keyboard.insertText('print("changed draft")');
    await expect(
        page.getByText(
            /Exercise 01: Attempted · Historical pass on this device/,
        ),
    ).toBeVisible();
    await page.reload();
    await page.getByText("Your exercise progress", { exact: true }).click();
    await expect(
        page.getByText(
            /Historical pass on this device; current draft is not approved/,
        ),
    ).toBeVisible();
});
