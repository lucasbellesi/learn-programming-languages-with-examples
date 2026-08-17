// Module focus: Tracking ownership and lifetime when multiple references can observe the same value.
// Why it matters: the example makes it possible to model exclusive, shared, and non-owning
// relationships idiomatically before the learner tackles the exercises.

// Separate helpers keep the main path focused on how to model exclusive, shared, and non-owning
// relationships idiomatically.
type Note = {
    id: string;
    body: string;
};

class NoteOwner {
    constructor(
        readonly label: string,
        private note: Note | null,
    ) {}

    transferTo(other: NoteOwner): void {
        // Moving ownership leaves the source empty and makes the destination responsible.
        if (this.note === null) {
            return;
        }

        other.note = this.note;
        this.note = null;
    }

    currentNote(): Note | null {
        // Returning the object shows that aliases can still observe shared mutable state.
        return this.note;
    }

    describe(): string {
        return this.note === null
            ? `${this.label} owns nothing`
            : `${this.label} owns ${this.note.id}`;
    }
}

// Fixed inputs make the consequence of treating object references as automatic deep copies
// visible and repeatable.
function main(): void {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    const originalNote: Note = {
        id: "note-101",
        body: "Review release checklist",
    };

    const inbox = new NoteOwner("inbox", originalNote);
    const archive = new NoteOwner("archive", null);

    // Print ownership before and after transfer so the lifetime change is visible.
    // The printed result shows whether the program can prevent leaks, cycles, and stale
    // observations in ownership graphs.
    console.log(inbox.describe());
    console.log(archive.describe());

    inbox.transferTo(archive);

    console.log(inbox.describe());
    console.log(archive.describe());

    const alias = archive.currentNote();
    if (alias !== null) {
        alias.body = "Review release checklist and publish notes";
        console.log(`Alias sees: ${alias.body}`);
    }
}

main();

export {};
