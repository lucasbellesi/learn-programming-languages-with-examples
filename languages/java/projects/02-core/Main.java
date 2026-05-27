import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    record StudentScore(String name, int score) {
    }

    static StudentScore parseRecord(String line) {
        String[] parts = line.trim().split("\\s+");
        if (parts.length < 3) {
            return null;
        }

        try {
            int score = Integer.parseInt(parts[parts.length - 1]);
            if (score < 0 || score > 100) {
                return null;
            }
            String name = String.join(" ", java.util.Arrays.copyOf(parts, parts.length - 1));
            return name.isBlank() ? null : new StudentScore(name, score);
        } catch (NumberFormatException error) {
            return null;
        }
    }

    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the input file path: ");
        Path sourcePath = Path.of(scanner.nextLine().trim());

        if (!Files.isRegularFile(sourcePath)) {
            System.out.println("Input file not found.");
            return;
        }

        List<StudentScore> validRecords = new ArrayList<>();
        int invalidRows = 0;

        for (String line : Files.readAllLines(sourcePath)) {
            if (line.isBlank()) {
                continue;
            }

            StudentScore record = parseRecord(line);
            if (record == null) {
                invalidRows++;
            } else {
                validRecords.add(record);
            }
        }

        Path reportPath = Path.of("report.txt");
        List<String> lines = new ArrayList<>();
        lines.add("Grade Report");
        lines.add("Source file: " + sourcePath);
        lines.add("Valid records: " + validRecords.size());
        lines.add("Invalid rows skipped: " + invalidRows);

        if (validRecords.isEmpty()) {
            lines.add("Average: N/A");
            lines.add("Students: none");
            System.out.println("Valid records: 0");
            System.out.println("Invalid rows skipped: " + invalidRows);
            System.out.println("Average: N/A");
        } else {
            double average = validRecords.stream().mapToInt(StudentScore::score).average().orElse(0.0);
            lines.add(String.format("Average: %.2f", average));
            lines.add("Students:");
            for (StudentScore record : validRecords) {
                lines.add("- " + record.name() + ": " + record.score());
            }
            System.out.println("Valid records: " + validRecords.size());
            System.out.println("Invalid rows skipped: " + invalidRows);
            System.out.printf("Average: %.2f%n", average);
        }

        Files.write(reportPath, lines);
        System.out.println("Report written to report.txt");
    }
}
