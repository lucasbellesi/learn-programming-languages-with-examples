// Module focus: Tracking ownership and lifetime when multiple references can observe the same value.
// Why it matters: practicing smart pointers in depth patterns makes exercises and checkpoints easier to reason about.

import java.lang.ref.WeakReference;
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

    static final class PreviewPane {
        private final WeakReference<Report> currentReport;

        PreviewPane(Report report) {
            // The preview can observe the report without becoming an owner.
            this.currentReport = new WeakReference<>(report);
        }

        void clearForDemo() {
            // Clearing the weak reference gives this small example deterministic output.
            currentReport.clear();
        }

        void describe() {
            Report report = currentReport.get();
            if (report == null) {
                System.out.println("Preview target expired.");
                return;
            }

            System.out.println("Preview can still see: " + report.title());
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

        Report transientDraft = new Report("Transient Draft");
        PreviewPane preview = new PreviewPane(transientDraft);
        preview.describe();

        // Weak observers must handle the target disappearing without owning it.
        transientDraft = null;
        preview.clearForDemo();
        preview.describe();
    }
}
