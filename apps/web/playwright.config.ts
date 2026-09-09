import { defineConfig } from "@playwright/test";

export default defineConfig({
    testDir: "./tests/browser",
    use: { baseURL: "http://127.0.0.1:3100", trace: "retain-on-failure" },
    webServer: {
        command: "npm run dev -- --hostname 127.0.0.1 --port 3100",
        url: "http://127.0.0.1:3100",
        reuseExistingServer: false,
        env: {
            EXECUTION_ENABLED: "false",
            NEXT_DIST_DIR: ".next-test",
            NEXT_PUBLIC_SUPABASE_URL: "",
            NEXT_PUBLIC_SUPABASE_ANON_KEY: "",
        },
        timeout: 120000,
    },
});
