import { test, after } from "node:test";
import assert from "node:assert/strict";
import { randomUUID } from "node:crypto";
import { readFile } from "node:fs/promises";
import { PGlite } from "@electric-sql/pglite";
const db = new PGlite();
await db.exec(`create role anon; create role authenticated; create role service_role bypassrls;
create schema auth; create table auth.users(id uuid primary key);
create function auth.uid() returns uuid language sql as $$ select nullif(current_setting('request.jwt.claim.sub',true),'')::uuid $$;
grant usage on schema auth,public to anon,authenticated,service_role;
grant execute on function auth.uid() to authenticated;
insert into auth.users values ('11111111-1111-4111-8111-111111111111'),('22222222-2222-4222-8222-222222222222');`);
await db.exec(
    await readFile(
        new URL(
            "../supabase/migrations/202609070001_learning_beta.sql",
            import.meta.url,
        ),
        "utf8",
    ),
);
await db.exec(
    "grant select,insert,update,delete on all tables in schema public to anon,authenticated,service_role;",
);
after(() => db.close());
const uid = "11111111-1111-4111-8111-111111111111";
async function reset() {
    await db.exec(
        "reset role; truncate public.executions,public.execution_quotas,public.drafts,public.progress;",
    );
}
async function reserve(
    identity = "guest:one",
    user = null,
    ip = "ip:one",
    key = randomUUID(),
    hash = "hash",
) {
    const { rows } = await db.query(
        "select public.reserve_execution($1,$2,$3,$4,$5,$6,$7,$8) as result",
        [
            identity,
            user,
            ip,
            key,
            hash,
            "python/01-foundations/types-and-io/01",
            "a".repeat(40),
            "check",
        ],
    );
    return rows[0].result;
}
async function finish(row, status = "passed") {
    return db.query("select public.finish_execution($1,$2,$3)", [
        row.execution.id,
        row.execution.identity,
        JSON.stringify({ status }),
    ]);
}
test("guest quota is five; idempotent retry does not reserve twice", async () => {
    await reset();
    const key = randomUUID();
    const first = await reserve("guest:one", null, "ip:one", key);
    const retry = await reserve("guest:one", null, "ip:one", key);
    assert.equal(retry.created, false);
    assert.equal(retry.execution.id, first.execution.id);
    await assert.rejects(
        reserve("guest:one", null, "ip:one", key, "different"),
        /conflicts/,
    );
    await finish(first);
    for (let i = 0; i < 4; i++) await finish(await reserve());
    await assert.rejects(reserve(), /Daily execution limit/);
});
test("global concurrency and one slot per identity", async () => {
    await reset();
    await reserve();
    await assert.rejects(reserve(), /already running/);
    for (let i = 2; i <= 4; i++) await reserve(`guest:${i}`, null, `ip:${i}`);
    await assert.rejects(
        reserve("guest:five", null, "ip:five"),
        /slots are busy/,
    );
    await db.exec("update executions set expires_at=now()-interval '1 second'");
    assert.equal((await reserve("guest:five", null, "ip:five")).created, true);
});
test("network quota survives guest cookie changes", async () => {
    await reset();
    for (let i = 0; i < 10; i++) await finish(await reserve(`guest:${i}`));
    await assert.rejects(reserve("guest:new"), /network daily limit/);
});
test("account quota is 25 and only completed checks produce verified progress", async () => {
    await reset();
    for (let i = 0; i < 25; i++)
        await finish(await reserve(`user:${uid}`, uid));
    await assert.rejects(reserve(`user:${uid}`, uid), /Daily execution limit/);
    assert.equal((await db.query("select * from progress")).rows.length, 1);
});
test("cancellation cannot be overwritten by late successful polling", async () => {
    await reset();
    const row = await reserve(`user:${uid}`, uid);
    await finish(row, "cancelled");
    await finish(row, "passed");
    assert.equal((await db.query("select * from progress")).rows.length, 0);
    assert.equal(
        (await db.query("select status from executions")).rows[0].status,
        "cancelled",
    );
});
test("RLS isolates drafts and prevents forged progress and quota RPC calls", async () => {
    await reset();
    await db.exec(`set role authenticated; set request.jwt.claim.sub='${uid}'`);
    await db.query(
        "insert into drafts(user_id,activity_id,code,revision) values($1,$2,$3,$4)",
        [
            uid,
            "python/01-foundations/types-and-io/01",
            "print(1)",
            "a".repeat(40),
        ],
    );
    await assert.rejects(
        db.query(
            "insert into progress(user_id,activity_id,revision) values($1,$2,$3)",
            [uid, "anything", "a"],
        ),
        /row-level security/,
    );
    await assert.rejects(reserve(), /permission denied/);
    await db.exec(
        "set request.jwt.claim.sub='22222222-2222-4222-8222-222222222222'",
    );
    assert.equal((await db.query("select * from drafts")).rows.length, 0);
    await db.exec("reset role; set role anon");
    assert.equal((await db.query("select * from drafts")).rows.length, 0);
    await db.exec("reset role");
});
