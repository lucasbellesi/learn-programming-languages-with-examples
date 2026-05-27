import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Exercise02 {
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
            return new StudentScore(name, score);
        } catch (NumberFormatException error) {
            return null;
        }
    }

    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        Path inputPath = Path.of(scanner.nextLine().trim());
        Path outputPath = Path.of(scanner.nextLine().trim());

        List<StudentScore> records = new ArrayList<>();
        int skipped = 0;
        for (String line : Files.readAllLines(inputPath)) {
            StudentScore record = parseRecord(line);
            if (record == null) {
                skipped++;
            } else {
                records.add(record);
            }
        }

        double average = records.stream().mapToInt(StudentScore::score).average().orElse(0.0);
        List<String> report = new ArrayList<>();
        report.add("Grade Report");
        report.add("Valid records: " + records.size());
        report.add("Invalid rows skipped: " + skipped);
        report.add(String.format("Average: %.2f", average));
        for (StudentScore record : records) {
            report.add("- " + record.name() + ": " + record.score());
        }
        Files.write(outputPath, report);

        System.out.println("Valid records: " + records.size());
        System.out.println("Invalid rows skipped: " + skipped);
        System.out.printf("Average: %.2f%n", average);
        System.out.println("Report written to " + outputPath);
    }
}
