import { openDB } from "idb";
import type { Journey } from "./guide-types";
export type Draft = {
    id: string;
    code: string;
    revision: string;
    updatedAt: string;
    passed?: boolean;
};
let connection: ReturnType<typeof openDB> | undefined;
const database = () => {
    if (connection) return connection;
    let blocked = false;
    let rejectBlocked: (reason: Error) => void = () => {};
    const unavailable = new Promise<never>((_, reject) => {
        rejectBlocked = reject;
    });
    const opening = openDB("programming-examples", 2, {
        upgrade(db) {
            for (const store of ["drafts", "journeys", "activityProgress"])
                if (!db.objectStoreNames.contains(store))
                    db.createObjectStore(store, { keyPath: "id" });
        },
        blocking() {
            void connection?.then((db) => db.close());
            connection = undefined;
        },
        terminated() {
            connection = undefined;
        },
        blocked() {
            blocked = true;
            rejectBlocked(
                new Error(
                    "Close older tabs of this site and reload to upgrade local storage.",
                ),
            );
        },
    });
    // A pre-upgrade tab may still hold version 1 open. Do not leave the guide
    // loading indefinitely, or apply a late load over answers entered meanwhile.
    connection = Promise.race([opening, unavailable]);
    void opening.then(
        (db) => {
            if (blocked) db.close();
        },
        () => {},
    );
    return connection;
};
export async function loadDraft(id: string): Promise<Draft | undefined> {
    return (await database()).get("drafts", id);
}
export async function saveDraft(draft: Draft) {
    await (await database()).put("drafts", draft);
    window.dispatchEvent(new Event("learning-progress"));
}
export async function allDrafts(): Promise<Draft[]> {
    return (await database()).getAll("drafts");
}
export async function loadJourney(id: string): Promise<Journey | undefined> {
    return (await database()).get("journeys", id);
}
export async function saveJourney(journey: Journey) {
    const db = await database();
    await db.put("journeys", journey);
}
export type ActivityProgress = {
    id: string;
    visitedAt?: string;
    attemptedAt?: string;
    passedAt?: string;
};
export async function recordActivity(
    id: string,
    kind: "visitedAt" | "attemptedAt" | "passedAt",
) {
    const db = await database();
    const tx = db.transaction("activityProgress", "readwrite");
    const previous = await tx.store.get(id);
    await tx.store.put({ ...previous, id, [kind]: new Date().toISOString() });
    await tx.done;
    window.dispatchEvent(new Event("learning-progress"));
}
export async function localActivityProgress(): Promise<ActivityProgress[]> {
    return (await database()).getAll("activityProgress");
}
