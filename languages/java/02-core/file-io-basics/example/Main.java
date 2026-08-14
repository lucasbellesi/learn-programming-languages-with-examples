// Module focus: Reading plain-text files, parsing rows, and writing clear results.
// Why it matters: practicing file io basics patterns makes exercises and checkpoints easier to reason about.

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        // Explicit paths make missing input observable instead of creating it silently.
        Path inputPath = Path.of(args.length > 0 ? args[0] : "example/fixtures/scores.txt");
        Path reportPath = Path.of(args.length > 1 ? args[1] : "build/report.txt");
        if (!Files.isRegularFile(inputPath)) {
            System.err.println("Input file not found: " + inputPath.toAbsolutePath());
            return;
        }

        List<ScoreReport.StudentScore> validRecords = new ArrayList<>();
        int skipped = 0;

        // Keep accepted and rejected records separate for transparent feedback.
        for (String line : Files.readAllLines(inputPath)) {
            if (line.isBlank()) {
                continue;
            }
            ScoreReport.StudentScore record = ScoreReport.parseRecord(line);
            if (record == null) {
                skipped++;
            } else {
                validRecords.add(record);
            }
        }

        // Persist and print the same report so both outputs can be compared directly.
        List<String> report = ScoreReport.build(validRecords, skipped);
        Path parent = reportPath.toAbsolutePath().getParent();
        if (parent != null) {
            Files.createDirectories(parent);
        }
        Files.write(reportPath, report);
        System.out.println("Report file: " + reportPath);
        report.forEach(System.out::println);
    }
}
