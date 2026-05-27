import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    static String bucketLabel(int start) {
        int end = start == 90 ? 100 : start + 9;
        return start + "-" + end;
    }

    static int bucketCount(List<Integer> scores, int start) {
        int end = start == 90 ? 100 : start + 9;
        int count = 0;
        for (int score : scores) {
            if (score >= start && score <= end) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        List<Integer> scores = new ArrayList<>();

        while (true) {
            System.out.print("Enter a score (0-100) or -1 to finish: ");
            if (!scanner.hasNext()) {
                break;
            }

            String raw = scanner.next().trim();
            int value;
            try {
                value = Integer.parseInt(raw);
            } catch (NumberFormatException error) {
                System.out.println("Invalid integer. Try again.");
                continue;
            }

            if (value == -1) {
                break;
            }
            if (value < 0 || value > 100) {
                System.out.println("Score ignored because it is outside 0-100.");
                continue;
            }
            scores.add(value);
        }

        List<String> lines = new ArrayList<>();
        lines.add("Valid scores: " + scores.size());

        if (scores.isEmpty()) {
            lines.add("Average: N/A");
            lines.add("Minimum: N/A");
            lines.add("Maximum: N/A");
        } else {
            int total = 0;
            int minimum = scores.get(0);
            int maximum = scores.get(0);
            for (int score : scores) {
                total += score;
                minimum = Math.min(minimum, score);
                maximum = Math.max(maximum, score);
            }
            lines.add(String.format("Average: %.2f", (double) total / scores.size()));
            lines.add("Minimum: " + minimum);
            lines.add("Maximum: " + maximum);
        }

        lines.add("Frequency:");
        for (int start = 0; start < 100; start += 10) {
            lines.add("- " + bucketLabel(start) + ": " + bucketCount(scores, start));
        }

        for (String line : lines) {
            System.out.println(line);
        }

        Path reportPath = Path.of("core_assessment_report.txt");
        Files.write(reportPath, lines);
        System.out.println("Report written to core_assessment_report.txt");
    }
}
