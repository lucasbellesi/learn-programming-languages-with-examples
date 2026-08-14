// Module focus: Moving one owned reference between explicit holders.
// Why it matters: managed runtimes still need clear ownership boundaries.

import java.util.Optional;

public class Exercise01 {
    record Document(String name) {
    }

    static final class DocumentSlot {
        private final String label;
        private Document current;

        DocumentSlot(String label, Document current) {
            this.label = label;
            this.current = current;
        }

        Optional<Document> current() {
            return Optional.ofNullable(current);
        }

        void moveTo(DocumentSlot destination) {
            if (current == null) {
                System.out.println(label + " is empty.");
                return;
            }

            System.out.println(label + " moves " + current.name() + " to " + destination.label + ".");
            destination.current = current;
            current = null;
        }

        void print() {
            System.out.println(label + ": " + current().map(Document::name).orElse("empty"));
        }
    }

    public static void main(String[] args) {
        DocumentSlot active = new DocumentSlot("Active", new Document("Roadmap"));
        DocumentSlot backup = new DocumentSlot("Backup", new Document("Old Notes"));
        DocumentSlot empty = new DocumentSlot("Empty", null);

        active.print();
        backup.print();
        active.moveTo(backup);
        active.print();
        backup.print();
        empty.moveTo(active);
        empty.print();
        active.print();
    }
}
