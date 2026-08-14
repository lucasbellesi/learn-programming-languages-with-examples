import java.lang.ref.WeakReference;

public class WeakObservation {
    record Report(String title) {
    }

    static final class PreviewPane {
        private final WeakReference<Report> currentReport;

        PreviewPane(Report report) {
            currentReport = new WeakReference<>(report);
        }

        void simulateExpiration() {
            // GC timing is nondeterministic, so this explicitly simulates an expired target.
            currentReport.clear();
        }

        void describe() {
            Report report = currentReport.get();
            System.out.println(
                    report == null ? "Preview target expired." : "Preview can still see: " + report.title());
        }
    }

    public static void main(String[] args) {
        Report transientDraft = new Report("Transient Draft");
        PreviewPane preview = new PreviewPane(transientDraft);
        preview.describe();
        preview.simulateExpiration();
        preview.describe();
    }
}
