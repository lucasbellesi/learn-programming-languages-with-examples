import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
test("guided exporter rejects broken references and incomplete questions", () => {
    const result = spawnSync("python", ["tests/test_guides.py"], {
        encoding: "utf8",
    });
    assert.equal(result.status, 0, result.stdout + result.stderr);
});
