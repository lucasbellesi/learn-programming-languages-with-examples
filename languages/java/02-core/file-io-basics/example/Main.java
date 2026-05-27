// Module focus: Reading plain-text files, parsing rows, and writing clear results.
// Why it matters: practicing file io basics patterns makes exercises and checkpoints easier to reason about.

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Main {
    record StudentScore(String name, int score) {
    }

    static StudentScore parseRecord(String line) {
        String[] parts = line.trim().split("\\s+");
        // A valid record needs at least a first name, last name, and numeric score.
        if (parts.length < 3) {
            return null;
        }

        try {
            int score = Integer.parseInt(parts[parts.length - 1]);
            // Domain validation stays beside parsing so invalid rows have one exit path.
            if (score < 0 || score > 100) {
                return null;
            }
            String name = String.join(" ", java.util.Arrays.copyOf(parts, parts.length - 1));
            return new StudentScore(name, score);
        } catch (NumberFormatException error) {
            // Returning null keeps the caller in charge of counting skipped records.
            return null;
        }
    }

    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Path inputPath = Path.of("scores.txt");
        Path reportPath = Path.of("report.txt");
        Files.write(inputPath, List.of("Ana Smith 91", "Bob Lee 77", "InvalidRow", "Carla Mendez 88"));

        List<StudentScore> validRecords = new ArrayList<>();
        int skipped = 0;
        for (String line : Files.readAllLines(inputPath)) {
            StudentScore record = parseRecord(line);
            // The main loop separates accepted records from malformed rows.
            if (record == null) {
                skipped++;
            } else {
                validRecords.add(record);
            }
        }

        double average = validRecords.stream().mapToInt(StudentScore::score).average().orElse(0.0);
        List<String> report = new ArrayList<>();
        report.add("Grade Report");
        report.add("Valid records: " + validRecords.size());
        report.add("Invalid rows skipped: " + skipped);
        report.add(String.format("Average: %.2f", average));
        for (StudentScore record : validRecords) {
            // Each accepted row is preserved in the report for easy manual checking.
            report.add("- " + record.name() + ": " + record.score());
        }
        Files.write(reportPath, report);

        // Report both console and file results so the transformation can be verified.
        System.out.println("Report file: " + reportPath);
        System.out.println("Valid records: " + validRecords.size());
        System.out.println("Invalid rows skipped: " + skipped);
        System.out.printf("Average: %.2f%n", average);
    }
}
