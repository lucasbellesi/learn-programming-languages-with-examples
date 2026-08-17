// Module focus: Moving one owned reference between explicit holders.
// Why it matters: managed runtimes still need clear ownership boundaries.

import java.util.Optional;
import java.util.Scanner;

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
            if (destination.current != null) {
                System.out.println(destination.label + " is occupied.");
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
        Scanner scanner = new Scanner(System.in);
        String sourceName = scanner.hasNextLine() ? scanner.nextLine() : "empty";
        String destinationName = scanner.hasNextLine() ? scanner.nextLine() : "empty";
        DocumentSlot active = new DocumentSlot(
                "Source", sourceName.equals("empty") ? null : new Document(sourceName));
        DocumentSlot backup = new DocumentSlot(
                "Destination", destinationName.equals("empty") ? null : new Document(destinationName));

        active.print();
        backup.print();
        active.moveTo(backup);
        active.print();
        backup.print();
    }
}
