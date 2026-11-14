import { test, expect } from "@playwright/test";

declare global {
    interface Window {
        policyViolations: string[];
    }
}

test("production CSP uses fresh nonces and blocks injected inline scripts", async ({
    page,
}) => {
    await page.addInitScript(() => {
        (window as Window & { policyViolations?: string[] }).policyViolations =
            [];
        document.addEventListener("securitypolicyviolation", (event) => {
            (
                window as Window & { policyViolations: string[] }
            ).policyViolations.push(event.effectiveDirective);
        });
    });
    const response = await page.goto("/");
    const policy = response!.headers()["content-security-policy"];
    const nonce = policy.match(/'nonce-([^']+)'/)![1];
    expect(policy).not.toMatch(/script-src[^;]*unsafe-(inline|eval)/);
    expect(policy).toContain("frame-ancestors 'none'");
    expect(response!.headers()["cache-control"]).toContain("no-store");
    await expect(page.getByLabel("Search concepts")).toBeVisible();
    expect(
        await page
            .locator("script:not([src])")
            .evaluateAll((scripts) =>
                scripts.every((script) =>
                    Boolean((script as HTMLScriptElement).nonce),
                ),
            ),
    ).toBe(true);
    expect(
        await page.evaluate(
            () =>
                (window as Window & { policyViolations: string[] })
                    .policyViolations,
        ),
    ).toEqual([]);
    await page.route("**/", async (route) => {
        const response = await route.fetch();
        const html = await response.text();
        await route.fulfill({
            response,
            body: html.replace(
                "</body>",
                "<script>window.untrustedInlineExecuted = true</script></body>",
            ),
        });
    });
    const fresh = await page.reload();
    await expect
        .poll(() =>
            page.evaluate(() =>
                window.policyViolations.some((directive) =>
                    directive.startsWith("script-src"),
                ),
            ),
        )
        .toBe(true);
    expect(
        await page.evaluate(
            () =>
                (window as Window & { untrustedInlineExecuted?: boolean })
                    .untrustedInlineExecuted,
        ),
    ).toBeUndefined();
    expect(fresh!.headers()["content-security-policy"]).not.toContain(
        `'nonce-${nonce}'`,
    );
});

test("CSP permits editor workers, theme changes and code downloads", async ({
    page,
}) => {
    const blocked: string[] = [];
    page.on("console", (message) => {
        if (/content.security.policy/i.test(message.text()))
            blocked.push(message.text());
    });
    await page.addInitScript(() => {
        window.policyViolations = [];
        document.addEventListener("securitypolicyviolation", (event) =>
            window.policyViolations.push(event.effectiveDirective),
        );
    });
    await page.goto("/learn/typescript/01-foundations/types-and-io");
    await expect(page.locator(".monaco-editor")).toBeVisible();
    const editor = page.getByRole("textbox", {
        name: "Code editor",
        exact: true,
    });
    await editor.press("ControlOrMeta+A");
    await page.keyboard.type(
        'const message: string = "CSP keeps drafts";\nconsole.log(message);\n',
    );
    await expect(page.getByRole("status")).toHaveText("Saved on this device");
    await expect.poll(() => page.workers().length).toBeGreaterThan(0);
    await page
        .getByRole("button", { name: "Theme: System", exact: true })
        .click();
    await expect(page.locator(".monaco-editor")).toHaveClass(/vs-dark/);
    const downloading = page.waitForEvent("download");
    await page.getByRole("button", { name: "Download ↓" }).click();
    expect((await downloading).suggestedFilename()).toBe("main.ts");
    expect(await page.evaluate(() => window.policyViolations)).toEqual([]);
    expect(blocked).toEqual([]);
});
