import { test } from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
const catalog = JSON.parse(
    await readFile(new URL("../generated/catalog.json", import.meta.url)),
);
const solutions = JSON.parse(
    await readFile(new URL("../generated/solutions.json", import.meta.url)),
);
test("complete catalog and foundations-only execution", () => {
    assert.equal(catalog.docs.length, 192);
    assert.equal(Object.keys(catalog.activities).length, 432);
    const enabled = Object.values(catalog.activities).filter((a) => a.enabled);
    assert.equal(enabled.filter((a) => a.kind === "example").length, 48);
    assert.equal(enabled.filter((a) => a.kind === "exercise").length, 96);
    assert.equal(new Set(catalog.docs.map((d) => d.id)).size, 192);
    for (const a of enabled) {
        assert.equal(a.revision, catalog.revision);
        assert.match(a.id, /\/01-foundations\//);
        assert.ok(a.source);
        if (a.kind === "exercise") {
            assert.ok(solutions[a.id]);
            assert.equal(a.hints.length, 3);
            assert.ok(a.cases.length > 0);
        }
    }
});
test("documents reference real activities and solutions are separate", () => {
    for (const doc of catalog.docs) {
        assert.ok(doc.markdown);
        for (const id of doc.activities) assert.ok(catalog.activities[id]);
    }
    for (const a of Object.values(catalog.activities))
        assert.equal(a.solution, undefined);
});
