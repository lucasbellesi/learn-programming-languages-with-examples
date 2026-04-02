// This example shows tracking ownership and lifetime when multiple references can observe the same value.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

// Define the reusable pieces first so the main flow can focus on one observable scenario.
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

// Run one deterministic scenario so the console output makes tracking ownership and lifetime when multiple references can observe the same value easy to verify.
function main(): void {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    const originalNote: Note = {
        id: "note-101",
        body: "Review release checklist",
    };

    const inbox = new NoteOwner("inbox", originalNote);
    const archive = new NoteOwner("archive", null);

    // Print the observed state here so learners can connect the code path to a concrete result.
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
