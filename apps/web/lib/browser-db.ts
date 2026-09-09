import { openDB } from "idb";
export type Draft = {
    id: string;
    code: string;
    revision: string;
    updatedAt: string;
    passed?: boolean;
};
const database = () =>
    openDB("programming-examples", 1, {
        upgrade(db) {
            db.createObjectStore("drafts", { keyPath: "id" });
        },
    });
export async function loadDraft(id: string): Promise<Draft | undefined> {
    return (await database()).get("drafts", id);
}
export async function saveDraft(draft: Draft) {
    return (await database()).put("drafts", draft);
}
export async function allDrafts(): Promise<Draft[]> {
    return (await database()).getAll("drafts");
}
