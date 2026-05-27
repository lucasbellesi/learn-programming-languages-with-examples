// Module focus: Rejecting invalid input before the main workflow continues.
// Why it matters: practicing input validation patterns makes exercises and checkpoints easier to reason about.

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Main {
    static boolean isValidScore(int score) {
        return score >= 0 && score <= 100;
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        String[] rawScores = {"91", "-4", "abc", "77"};
        List<Integer> accepted = new ArrayList<>();
        int skipped = 0;

        // Parse and validate each token separately so one bad value does not stop the run.
        for (String rawScore : rawScores) {
            try {
                int score = Integer.parseInt(rawScore);
                // Successful parsing still needs a domain check before accepting the value.
                if (isValidScore(score)) {
                    accepted.add(score);
                } else {
                    skipped++;
                }
            } catch (NumberFormatException error) {
                // Bad text is counted and skipped instead of ending the whole workflow.
                skipped++;
            }
        }

        double average = accepted.stream().mapToInt(Integer::intValue).average().orElse(0.0);

        // Report accepted values and skipped records as observable validation evidence.
        System.out.println("Accepted: " + accepted);
        System.out.println("Skipped: " + skipped);
        System.out.printf("Average: %.2f%n", average);
    }
}
