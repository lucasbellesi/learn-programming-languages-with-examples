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

function main(): void {
    const originalNote: Note = {
        id: "note-101",
        body: "Review release checklist",
    };

    const inbox = new NoteOwner("inbox", originalNote);
    const archive = new NoteOwner("archive", null);

    console.log(inbox.describe());
    console.log(archive.describe());

    // Intent: model a move by handing over the reference and clearing the old owner.
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
