// Local assessment of trusted repository code. Fixtures never contact cloud services.
import assert from "node:assert/strict";
import { createRequire } from "node:module";
import { readFile, mkdir, writeFile } from "node:fs/promises";
import { execFileSync } from "node:child_process";
import { runInNewContext } from "node:vm";
import ts from "typescript";
import { PGlite } from "@electric-sql/pglite";
import { chromium } from "@playwright/test";

const require = createRequire(import.meta.url);
const root = new URL("../", import.meta.url);
const checks = [];
const observations = [];
const revision = execFileSync("git", ["rev-parse", "HEAD"], {
    encoding: "utf8",
}).trim();
async function check(name, layer, action) {
    try {
        await action();
        checks.push({ name, layer, status: "passed" });
    } catch (error) {
        checks.push({ name, layer, status: "failed", error: error.message });
    }
}

// Transpile and execute fixed, trusted source paths with explicit service doubles.
// This VM is a test harness, not a sandbox for untrusted learner code.
async function load(path, dependencies = {}, env = {}) {
    const source = await readFile(new URL(path, root), "utf8");
    const compiled = ts.transpileModule(source, {
        compilerOptions: {
            module: ts.ModuleKind.CommonJS,
            target: ts.ScriptTarget.ES2022,
        },
    }).outputText;
    const module = { exports: {} };
    runInNewContext(
        compiled,
        {
            exports: module.exports,
            module,
            require(name) {
                if (Object.hasOwn(dependencies, name))
                    return dependencies[name];
                if (name.startsWith("node:") || name === "zod")
                    return require(name);
                throw Error(`Unexpected dependency: ${name}`);
            },
            process: { env },
            Buffer,
            URL,
            Request,
            Response,
            AbortSignal,
            console: { error() {} },
        },
        { filename: path },
    );
    return module.exports;
}
const env = {
    NODE_ENV: "production",
    EXECUTION_ENABLED: "true",
    NEXT_PUBLIC_SUPABASE_URL: "https://provider.invalid",
    NEXT_PUBLIC_SUPABASE_ANON_KEY: "fixture-public-key",
    SUPABASE_SERVICE_ROLE_KEY: "fixture-service-key",
    SESSION_SECRET: "fixture-secret-with-more-than-32-bytes",
    SANDBOX_SNAPSHOT_ID: "fixture-snapshot",
    VERCEL: "1",
};
let cookie;
let cookieOptions;
let currentUser = null;
let providerError = false;
const server = await load(
    "lib/server.ts",
    {
        "server-only": {},
        "@supabase/ssr": {
            createServerClient: () => ({
                auth: {
                    getUser: async () => ({
                        data: { user: currentUser },
                        error: null,
                    }),
                    exchangeCodeForSession: async () => {
                        if (providerError)
                            throw Error("fixture provider outage");
                        return { error: null };
                    },
                },
            }),
        },
        "@supabase/supabase-js": {
            createClient: () => {
                throw Error("Cloud access forbidden");
            },
        },
        "next/headers": {
            cookies: async () => ({
                get: () => (cookie ? { value: cookie } : undefined),
                set(name, value, options) {
                    cookie = value;
                    cookieOptions = options;
                },
                getAll: () => [],
            }),
        },
    },
    env,
);
const url = "https://app.example";
const request = (path, method = "GET", body, origin = url) =>
    new Request(url + path, {
        method,
        headers: {
            host: "app.example",
            origin,
            "x-vercel-forwarded-for": "192.0.2.10",
        },
        ...(body === undefined ? {} : { body: JSON.stringify(body) }),
    });
await check("CSRF origin rejection matrix", "source fixture", () => {
    server.sameOrigin(request("/", "POST"));
    for (const origin of [
        "https://evil.example",
        "null",
        "",
        "http://app.example",
        "https://app.example.evil.example",
        "https://app.example/",
        "https://app.example:444",
    ]) {
        assert.throws(() =>
            server.sameOrigin(request("/", "POST", undefined, origin)),
        );
    }
});
await check(
    "Forged guest signature rotates the identity and uses secure cookies",
    "source fixture",
    async () => {
        cookie = "11111111-1111-4111-8111-111111111111." + "0".repeat(64);
        const owner = await server.identity(request("/"));
        assert.notEqual(owner.id, "guest:11111111-1111-4111-8111-111111111111");
        assert.equal(cookieOptions.httpOnly, true);
        assert.equal(cookieOptions.secure, true);
        assert.equal(cookieOptions.sameSite, "lax");
        assert.equal((await server.identity(request("/"))).id, owner.id);
    },
);
await check(
    "Missing trusted network identity fails closed",
    "source fixture",
    async () => {
        const req = request("/");
        req.headers.delete("x-vercel-forwarded-for");
        await assert.rejects(
            () => server.identity(req),
            /Cannot verify guest network/,
        );
    },
);
await check(
    "Signed-in identity comes from verified provider user",
    "source fixture",
    async () => {
        currentUser = { id: "11111111-1111-4111-8111-111111111111" };
        assert.equal(
            (await server.identity(request("/"))).id,
            `user:${currentUser.id}`,
        );
        currentUser = null;
    },
);
env.SESSION_SECRET = "x";
cookie =
    "33333333-3333-4333-8333-333333333333." +
    server.digest("33333333-3333-4333-8333-333333333333");
observations.push({
    id: "S02",
    observation: "Execution accepts a one-byte session secret",
    accepted: server.executionConfigured(),
    chosenGuestAccepted:
        (await server.identity(request("/"))).id ===
        "guest:33333333-3333-4333-8333-333333333333",
});
env.SESSION_SECRET = "fixture-secret-with-more-than-32-bytes";

const catalog = JSON.parse(
    await readFile(new URL("generated/catalog.json", root), "utf8"),
);
const activity = Object.values(catalog.activities).find(
    (a) => a.enabled && a.kind === "exercise",
);
const owner = { id: "guest:fixture", userId: null, ip: "ip:fixture" };
let dbCalls = 0;
let sandboxCalls = 0;
let written;
const commands = [];
const db = {
    async rpc() {
        dbCalls++;
        return {
            data: {
                created: true,
                execution: {
                    id: "11111111-1111-4111-8111-111111111111",
                    expires_at: new Date(Date.now() + 55000).toISOString(),
                },
            },
            error: null,
        };
    },
    from() {
        return {
            update() {
                return { eq: async () => ({ error: null }) };
            },
        };
    },
};
const execution = await load(
    "app/api/executions/route.ts",
    {
        "@/lib/server": {
            ...server,
            identity: async () => owner,
            admin: () => db,
        },
        "@/lib/catalog": { catalog },
        "@/lib/executions": { finish: async () => {} },
        "@vercel/sandbox": {
            Sandbox: {
                create: async () => {
                    sandboxCalls++;
                    return {
                        name: "fixture",
                        writeFiles: async (files) => {
                            written = JSON.parse(files[0].content.toString());
                        },
                        runCommand: async (command) => {
                            commands.push(command);
                            return { exitCode: 0, cmdId: "fixture" };
                        },
                        stop: async () => {},
                    };
                },
            },
        },
    },
    env,
);
const payload = {
    activityId: activity.id,
    revision: catalog.revision,
    code: "print('fixture')",
    stdin: "",
    mode: "check",
    key: "11111111-1111-4111-8111-111111111111",
};
await check(
    "Cross-origin execution does not reserve quota or start a sandbox",
    "source fixture",
    async () => {
        const response = await execution.POST(
            request("/api/executions", "POST", payload, "https://evil.example"),
        );
        assert.notEqual(response.status, 202);
        assert.equal(dbCalls, 0);
        assert.equal(sandboxCalls, 0);
    },
);
await check(
    "Unknown activity, stale revision and oversized code are rejected before admission",
    "source fixture",
    async () => {
        for (const patch of [
            { activityId: "../../etc/passwd" },
            { revision: "stale" },
            { code: "x".repeat(65537) },
            { mode: "root-shell" },
        ]) {
            const response = await execution.POST(
                request("/api/executions", "POST", { ...payload, ...patch }),
            );
            assert.notEqual(response.status, 202);
        }
        assert.equal(dbCalls, 0);
        assert.equal(sandboxCalls, 0);
    },
);
await check(
    "Client commands, paths and grading rules cannot override trusted execution metadata",
    "source fixture",
    async () => {
        const response = await execution.POST(
            request("/api/executions", "POST", {
                ...payload,
                command: "attacker-command",
                filename: "../../etc/passwd",
                cases: [{ expected: "forged" }],
                language: "shell",
                userId: "attacker",
            }),
        );
        assert.equal(response.status, 202);
        assert.deepEqual(
            JSON.parse(JSON.stringify(written.cases)),
            activity.cases,
        );
        assert.equal(written.language, activity.language);
        assert.equal(written.filename, activity.path.split("/").at(-1));
        assert.deepEqual(
            commands.map((c) => c.cmd),
            ["install", "python3.12"],
        );
    },
);
await check(
    "Body-limit observation uses a bounded 256 KiB stream",
    "source fixture",
    async () => {
        let chunks = 0;
        const req = new Request(url + "/api/executions", {
            method: "POST",
            headers: { origin: url, host: "app.example" },
            duplex: "half",
            body: new ReadableStream(
                {
                    pull(controller) {
                        if (chunks === 32) return controller.close();
                        chunks++;
                        controller.enqueue(new Uint8Array(8192).fill(120));
                    },
                },
                { highWaterMark: 0 },
            ),
        });
        const before = dbCalls;
        const response = await execution.POST(req);
        assert.equal(response.status, 413);
        assert.equal(dbCalls, before);
        observations.push({
            id: "S01",
            bytesRead: chunks * 8192,
            declaredLimit: 100000,
            status: response.status,
        });
    },
);
await check(
    "Execution IDOR checks both job ID and current owner before inspection",
    "source fixture",
    async () => {
        const filters = [];
        let inspected = false;
        const route = await load("app/api/executions/[id]/route.ts", {
            "@/lib/server": {
                ...server,
                identity: async () => owner,
                admin: () => ({
                    from: () => ({
                        select: () => ({
                            eq(key, value) {
                                filters.push([key, value]);
                                return this;
                            },
                            single: async () => ({ data: null, error: null }),
                        }),
                    }),
                }),
            },
            "@/lib/executions": {
                inspect: async () => {
                    inspected = true;
                },
            },
        });
        const id = "22222222-2222-4222-8222-222222222222";
        const response = await route.GET(request(`/api/executions/${id}`), {
            params: Promise.resolve({ id }),
        });
        assert.equal(response.status, 404);
        assert.deepEqual(filters, [
            ["id", id],
            ["identity", owner.id],
        ]);
        assert.equal(inspected, false);
    },
);
await check(
    "Anonymous draft reads and writes are rejected",
    "source fixture",
    async () => {
        const drafts = await load("app/api/drafts/route.ts", {
            "@/lib/server": server,
            "@/lib/catalog": { catalog },
        });
        assert.equal((await drafts.GET()).status, 401);
        assert.equal(
            (await drafts.PUT(request("/api/drafts", "PUT", {}))).status,
            401,
        );
    },
);
await check(
    "OAuth callback ignores an attacker-controlled redirect target",
    "source fixture",
    async () => {
        const callback = await load("app/auth/callback/route.ts", {
            "@/lib/server": server,
        });
        const response = await callback.GET(
            request("/auth/callback?code=fixture&next=https://evil.example"),
        );
        assert.equal(response.headers.get("location"), "/");
        providerError = true;
        try {
            await callback.GET(request("/auth/callback?code=fixture"));
        } catch {
            observations.push({
                id: "S05",
                observation:
                    "Provider outage escapes the OAuth route without a handled Response",
            });
        }
        providerError = false;
    },
);

const database = new PGlite();
await check(
    "RLS blocks cross-user reads, updates, deletes and forged ownership",
    "local PostgreSQL",
    async () => {
        await database.exec(`create role anon; create role authenticated; create role service_role bypassrls;
        create schema auth; create table auth.users(id uuid primary key);
        create function auth.uid() returns uuid language sql as $$ select nullif(current_setting('request.jwt.claim.sub',true),'')::uuid $$;
        grant usage on schema auth,public to anon,authenticated,service_role;
        grant execute on function auth.uid() to authenticated;
        insert into auth.users values ('11111111-1111-4111-8111-111111111111'),('22222222-2222-4222-8222-222222222222');`);
        await database.exec(
            await readFile(
                new URL(
                    "supabase/migrations/202609070001_learning_beta.sql",
                    root,
                ),
                "utf8",
            ),
        );
        const first = "11111111-1111-4111-8111-111111111111";
        await database.exec(
            `set role authenticated; set request.jwt.claim.sub='${first}'`,
        );
        const injection = "'; drop table public.drafts; --";
        await database.query(
            "insert into drafts(user_id,activity_id,code,revision) values($1,$2,$3,$4)",
            [first, "fixture", injection, "a".repeat(40)],
        );
        await database.exec(
            "set request.jwt.claim.sub='22222222-2222-4222-8222-222222222222'",
        );
        assert.equal(
            (await database.query("select * from drafts")).rows.length,
            0,
        );
        assert.equal(
            (
                await database.query(
                    "update drafts set code='tampered' returning *",
                )
            ).rows.length,
            0,
        );
        assert.equal(
            (await database.query("delete from drafts returning *")).rows
                .length,
            0,
        );
        await assert.rejects(() =>
            database.query(
                "insert into drafts(user_id,activity_id,code,revision) values($1,$2,$3,$4)",
                [first, "forged", "x", "a"],
            ),
        );
        await assert.rejects(() =>
            database.exec(
                "insert into progress(user_id,activity_id,revision) values('22222222-2222-4222-8222-222222222222','forged','a')",
            ),
        );
        await assert.rejects(() => database.exec("select * from executions"));
        await assert.rejects(() =>
            database.exec("select * from execution_quotas"),
        );
        await assert.rejects(() =>
            database.exec(
                "select finish_execution(gen_random_uuid(),'forged','{}')",
            ),
        );
        await database.exec("reset role; set role anon");
        await assert.rejects(() => database.exec("select * from drafts"));
        await database.exec("reset role");
        assert.equal(
            (await database.query("select code from drafts")).rows[0].code,
            injection,
        );
    },
);
await check(
    "Deterministic cancellation/start interleaving observation",
    "source fixture + local PostgreSQL",
    async () => {
        let job;
        const adapter = {
            async rpc(name, values) {
                assert.equal(name, "reserve_execution");
                const { rows } = await database.query(
                    "select reserve_execution($1,$2,$3,$4,$5,$6,$7,$8) as result",
                    [
                        values.p_identity,
                        values.p_user_id,
                        values.p_ip,
                        values.p_key,
                        values.p_hash,
                        values.p_activity,
                        values.p_revision,
                        values.p_mode,
                    ],
                );
                job = rows[0].result.execution;
                return { data: rows[0].result, error: null };
            },
            from(table) {
                assert.equal(table, "executions");
                return {
                    update(record) {
                        return {
                            async eq(column, id) {
                                assert.equal(column, "id");
                                const entries = Object.entries(record);
                                assert.ok(
                                    entries.every(([key]) =>
                                        [
                                            "sandbox_id",
                                            "command_id",
                                            "status",
                                        ].includes(key),
                                    ),
                                );
                                await database.query(
                                    `update executions set ${entries.map(([key], i) => `${key}=$${i + 1}`).join(",")} where id=$${entries.length + 1}`,
                                    [...entries.map(([, value]) => value), id],
                                );
                                return { error: null };
                            },
                        };
                    },
                };
            },
        };
        const route = await load(
            "app/api/executions/route.ts",
            {
                "@/lib/server": {
                    ...server,
                    identity: async () => owner,
                    admin: () => adapter,
                },
                "@/lib/catalog": { catalog },
                "@/lib/executions": { finish: async () => {} },
                "@vercel/sandbox": {
                    Sandbox: {
                        create: async () => ({
                            name: "fixture",
                            writeFiles: async () => {},
                            stop: async () => {},
                            runCommand: async (command) => {
                                if (command.cmd === "python3.12") {
                                    await database.query(
                                        "select finish_execution($1,$2,$3)",
                                        [
                                            job.id,
                                            owner.id,
                                            JSON.stringify({
                                                status: "cancelled",
                                            }),
                                        ],
                                    );
                                }
                                return {
                                    exitCode: 0,
                                    cmdId: "fixture-command",
                                };
                            },
                        }),
                    },
                },
            },
            env,
        );
        const response = await route.POST(
            request("/api/executions", "POST", payload),
        );
        assert.equal(response.status, 202);
        const row = (
            await database.query(
                "select status,result from executions where id=$1",
                [job.id],
            )
        ).rows[0];
        observations.push({ id: "S06", afterCancellation: row });
    },
);
await database.close();

const argument = process.argv.find((a) => a.startsWith("--url="));
if (argument) {
    const target = new URL(argument.slice(6));
    if (
        target.protocol !== "http:" ||
        !["127.0.0.1", "localhost"].includes(target.hostname)
    )
        throw Error("Active probes require an explicit loopback HTTP URL");
    await check(
        "Production HTTP headers and sensitive path probes",
        "local production HTTP",
        async () => {
            const response = await fetch(target);
            assert.equal(response.status, 200);
            assert.equal(
                response.headers.get("x-content-type-options"),
                "nosniff",
            );
            assert.equal(response.headers.get("x-frame-options"), "DENY");
            assert.equal(response.headers.get("x-powered-by"), null);
            observations.push({
                id: "S03",
                contentSecurityPolicy: response.headers.get(
                    "content-security-policy",
                ),
            });
            for (const path of [
                "/.env",
                "/.env.local",
                "/.git/config",
                "/package.json",
                "/api/solution?id=../../.env.local",
            ]) {
                const result = await fetch(new URL(path, target));
                assert.equal(result.status, 404, path);
            }
            const callback = await fetch(
                new URL("/auth/callback?next=https://evil.example", target),
                { redirect: "manual" },
            );
            assert.equal(
                callback.headers.get("location"),
                "/?auth=unavailable",
            );
            const capability = await fetch(
                new URL("/api/capabilities", target),
            );
            assert.equal((await capability.json()).execution, false);
            assert.match(capability.headers.get("cache-control"), /no-store/);
            assert.equal(
                (await fetch(new URL("/api/drafts", target))).status,
                401,
            );
        },
    );
    await check(
        "Reflected input and console output stay inert; private canaries do not reach browser bundles",
        "local Chromium",
        async () => {
            const browser = await chromium.launch();
            try {
                const page = await browser.newPage();
                const bundles = [];
                await page.route("**/*", (route) =>
                    new URL(route.request().url()).origin === target.origin
                        ? route.continue()
                        : route.abort(),
                );
                page.on("response", (response) => {
                    if (
                        response.url().includes("/_next/") &&
                        response.url().split("?")[0].endsWith(".js")
                    )
                        bundles.push(response.text());
                });
                const attack = '<img src=x onerror="window.__owaspProbe=1">';
                await page.goto(target.href);
                await page.getByLabel("Search concepts").fill(attack);
                assert.equal(await page.locator("#curriculum img").count(), 0);
                await page.route("**/api/capabilities", (route) =>
                    route.fulfill({
                        json: { execution: true, message: "Local fixture" },
                    }),
                );
                await page.route("**/api/executions", (route) =>
                    route.fulfill({
                        status: 202,
                        json: { id: "probe", status: "running" },
                    }),
                );
                await page.route("**/api/executions/probe", (route) =>
                    route.fulfill({
                        json: {
                            status: "failed",
                            cases: [
                                {
                                    name: "XSS fixture",
                                    stdout: attack,
                                    stderr: attack,
                                    expected: attack,
                                    input: attack,
                                    passed: false,
                                },
                            ],
                        },
                    }),
                );
                await page.goto(
                    new URL("/learn/python/01-foundations/types-and-io", target)
                        .href,
                );
                await page.getByRole("button", { name: "Run code" }).click();
                await page
                    .getByText("× XSS fixture", { exact: true })
                    .waitFor();
                assert.equal(await page.locator(".results img").count(), 0);
                assert.equal(
                    await page.evaluate(() => window.__owaspProbe),
                    undefined,
                );
                const scripts = (await Promise.all(bundles)).join("\n");
                assert.ok(scripts.length > 1000);
                assert.ok(
                    !scripts.includes("owasp-private-canary-do-not-publish"),
                );
                assert.ok(
                    !scripts.includes("owasp-session-canary-do-not-publish"),
                );
            } finally {
                await browser.close();
            }
        },
    );
}
const output = new URL("build/owasp-check.json", root);
await mkdir(new URL("build/", root), { recursive: true });
await writeFile(
    output,
    JSON.stringify(
        { revision, checkedAt: new Date().toISOString(), checks, observations },
        null,
        2,
    ) + "\n",
);
console.log(
    JSON.stringify({ checks, observations, report: output.pathname }, null, 2),
);
if (checks.some((c) => c.status === "failed")) process.exitCode = 1;
