// Module focus: Tracking ownership and lifetime when multiple references can observe the same value.
// Why it matters: the example makes it possible to model exclusive, shared, and non-owning
// relationships idiomatically before the learner tackles the exercises.

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class Main {
    record Report(String title) {
    }

    static final class ReportOwner {
        private final String name;
        private Report current;

        ReportOwner(String name, Report current) {
            this.name = name;
            this.current = current;
        }

        Optional<Report> current() {
            // Optional keeps "empty owner" checks explicit at API boundaries.
            return Optional.ofNullable(current);
        }

        void transferTo(ReportOwner destination) {
            // Empty owners cannot transfer ownership, so the method exits visibly.
            if (current == null) {
                System.out.println(name + " has nothing to transfer.");
                return;
            }

            // Moving the reference leaves the source empty and the destination responsible.
            System.out.println(name + " transfers " + current.title() + " to " + destination.name + ".");
            destination.current = current;
            current = null;
        }

        void describe() {
            System.out.println(name + ": " + current().map(Report::title).orElse("empty"));
        }
    }

    static final class ReportArchive {
        private final List<Report> reports = new ArrayList<>();

        void add(Report report) {
            // Strong references in this list keep archived reports alive.
            reports.add(report);
        }

        List<Report> snapshot() {
            // A defensive snapshot prevents callers from mutating archive internals.
            return List.copyOf(reports);
        }
    }

    public static void main(String[] args) {
        ReportOwner inbox = new ReportOwner("Inbox", new Report("Quarterly Summary"));
        ReportOwner archiveSlot = new ReportOwner("Archive", null);

        // Report ownership before and after transfer so the lifetime change is visible.
        inbox.describe();
        archiveSlot.describe();
        inbox.transferTo(archiveSlot);
        inbox.describe();
        archiveSlot.describe();

        ReportArchive archive = new ReportArchive();
        archiveSlot.current().ifPresent(archive::add);
        archive.add(new Report("Budget Notes"));
        // The snapshot is safe to share because callers cannot mutate archive internals.
        System.out.println("Archive snapshot size: " + archive.snapshot().size());

    }
}
