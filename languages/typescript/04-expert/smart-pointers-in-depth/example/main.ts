// Module focus: Tracking ownership and lifetime when multiple references can observe the same value.
// Why it matters: practicing smart pointers in depth patterns makes exercises and checkpoints easier to reason about.

// Helper setup for smart pointers in depth; this keeps the walkthrough readable.
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
        if (this.note === null) {
            return;
        }

        other.note = this.note;
        this.note = null;
    }

    currentNote(): Note | null {
        return this.note;
    }

    describe(): string {
        return this.note === null
            ? `${this.label} owns nothing`
            : `${this.label} owns ${this.note.id}`;
    }
}

// Walk through one fixed scenario so smart pointers in depth behavior stays repeatable.
function main(): void {
    // Prepare sample inputs that exercise the key smart pointers in depth path.
    const originalNote: Note = {
        id: "note-101",
        body: "Review release checklist",
    };

    const inbox = new NoteOwner("inbox", originalNote);
    const archive = new NoteOwner("archive", null);

    // Report values so learners can verify the smart pointers in depth outcome.
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
