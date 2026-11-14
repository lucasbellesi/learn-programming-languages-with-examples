import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
    testDir: "./tests/browser",
    forbidOnly: Boolean(process.env.CI),
    workers: 2,
    globalTimeout: 10 * 60 * 1000,
    reporter: [["list"], ["html", { open: "never" }]],
    use: {
        baseURL: "http://127.0.0.1:3100",
        trace: "retain-on-failure",
        screenshot: "only-on-failure",
    },
    projects: [
        { name: "chromium", use: { ...devices["Desktop Chrome"] } },
        { name: "firefox", use: { ...devices["Desktop Firefox"] } },
        {
            name: "mobile-chromium",
            use: { ...devices["Pixel 7"] },
            testMatch: "**/curriculum.spec.ts",
        },
    ],
    webServer: {
        command:
            "npm run build && npm run start -- --hostname 127.0.0.1 --port 3100",
        url: "http://127.0.0.1:3100",
        reuseExistingServer: false,
        stdout: "pipe",
        env: {
            EXECUTION_ENABLED: "false",
            NEXT_DIST_DIR: ".next-test",
            NEXT_PUBLIC_SUPABASE_URL: "",
            NEXT_PUBLIC_SUPABASE_ANON_KEY: "",
        },
        timeout: 240000,
    },
});
