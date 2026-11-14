import { test, expect } from "@playwright/test";

test("search filters concepts and recovers from an empty result", async ({
    page,
}) => {
    const errors: string[] = [];
    page.on("pageerror", (error) => errors.push(error.message));
    await page.goto("/");
    await expect(page.getByRole("heading", { level: 1 })).toContainText(
        "Small examples.",
    );
    await page.getByRole("link", { name: "Find your starting point" }).click();
    await expect(page).toHaveURL(/#curriculum$/);
    const cards = page.locator("a.module-card");
    const search = page.getByRole("textbox", { name: "Search concepts" });
    await search.fill("TYPES-AND-IO");
    await expect(cards).toHaveCount(1);
    await expect(cards).toHaveAttribute(
        "href",
        "/learn/python/01-foundations/types-and-io",
    );
    await search.fill("no-such-concept-123");
    await expect(cards).toHaveCount(0);
    await expect(
        page.getByText("No concepts match this search."),
    ).toBeVisible();
    await search.clear();
    await expect(cards).toHaveCount(10);
    expect(errors).toEqual([]);
});

test("all six languages expose modules, projects, and assessments", async ({
    page,
}) => {
    await page.goto("/");
    for (const [id, name] of [
        ["cpp", "C++"],
        ["csharp", "C#"],
        ["go", "Go"],
        ["java", "Java"],
        ["python", "Python"],
        ["typescript", "TypeScript"],
    ]) {
        // Scope by the visible language name; icons can repeat the same text.
        const button = page.locator("button.language").filter({
            has: page.locator("strong").filter({
                hasText: new RegExp(`^${name.replace(/[+#]/g, "\\$&")}$`),
            }),
        });
        await button.click();
        await expect(button).toHaveAttribute("aria-pressed", "true");
        const cards = page.locator("a.module-card");
        await expect(cards).toHaveCount(10);
        await expect(
            page.locator(
                `a.module-card[href="/learn/${id}/01-foundations/types-and-io"]`,
            ),
        ).toBeVisible();
        await expect(
            page.locator(
                `a.module-card[href="/learn/${id}/01-foundations/project"]`,
            ),
        ).toBeVisible();
        await expect(
            page.locator(
                `a.module-card[href="/learn/${id}/01-foundations/assessment"]`,
            ),
        ).toBeVisible();
    }
    await page.getByRole("button", { name: "02 Core" }).click();
    await expect(page.locator("a.module-card")).toHaveCount(8);
    await expect(page.locator("a.module-card").first()).toHaveAttribute(
        "href",
        /\/typescript\/02-core\//,
    );
});

test("a catalog link opens a readable lesson and returns to the curriculum", async ({
    page,
}) => {
    await page.goto("/");
    await page
        .getByRole("textbox", { name: "Search concepts" })
        .fill("types-and-io");
    await page.locator("a.module-card").click();
    await expect(page).toHaveURL(
        /\/learn\/python\/01-foundations\/types-and-io$/,
    );
    await expect(page.getByRole("heading", { level: 1 })).toContainText(
        "Types and Input/Output",
    );
    await expect(page.locator("article.reading")).toContainText(
        "Learning Outcomes",
    );
    await expect(page.getByLabel("Language for this concept")).toHaveValue(
        "python",
    );
    expect(
        await page.evaluate(
            () => document.documentElement.scrollWidth <= innerWidth,
        ),
    ).toBe(true);
    await expect(page.getByRole("status", { includeHidden: true })).toHaveText(
        "Saved on this device",
    );
    await page.getByRole("link", { name: "← Back to the curriculum" }).click();
    await expect(page).toHaveURL("/");
    await expect(
        page.getByRole("textbox", { name: "Search concepts" }),
    ).toBeVisible();
});

test("unknown lessons return a real 404", async ({ page }) => {
    const response = await page.goto(
        "/learn/python/01-foundations/no-such-concept",
    );
    expect(response?.status()).toBe(404);
    await expect(
        page.getByRole("heading", { name: "404", exact: true }),
    ).toBeVisible();
});
