import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Locale;

final class ScoreReport {
    record StudentScore(String name, int score) {
    }

    private ScoreReport() {
    }

    static StudentScore parseRecord(String line) {
        // Parsing is isolated from file access so invalid rows have one clear policy.
        String[] parts = line.trim().split("\\s+");
        if (parts.length < 2) {
            return null;
        }
        try {
            int score = Integer.parseInt(parts[parts.length - 1]);
            String name = String.join(" ", Arrays.copyOf(parts, parts.length - 1));
            return score >= 0 && score <= 100 && !name.isBlank()
                    ? new StudentScore(name, score)
                    : null;
        } catch (NumberFormatException error) {
            return null;
        }
    }

    static List<String> build(List<StudentScore> records, int invalidRows) {
        List<String> lines = new ArrayList<>();
        lines.add("Grade Report");
        lines.add("Valid records: " + records.size());
        lines.add("Invalid rows skipped: " + invalidRows);
        if (records.isEmpty()) {
            lines.add("No valid records.");
            return lines;
        }

        double average = records.stream().mapToInt(StudentScore::score).average().orElse(0.0);
        lines.add(String.format(Locale.US, "Average: %.2f", average));
        for (StudentScore record : records) {
            lines.add("- " + record.name() + ": " + record.score());
        }
        return lines;
    }
}
