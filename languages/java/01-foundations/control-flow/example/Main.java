// Module focus: Choosing between branches and repeating work with predictable control flow.
// Why it matters: practicing control flow patterns makes exercises and checkpoints easier to reason about.

public class Main {
    public static void main(String[] args) {
        int[] scores = {91, 77, 88, 45};
        int passing = 0;
        int needsReview = 0;

        // Each branch explains one business rule for classifying a score.
        for (int score : scores) {
            if (score >= 60) {
                passing++;
            } else {
                needsReview++;
            }
        }

        // Report both branch outcomes so the loop logic can be checked directly.
        System.out.println("Passing: " + passing);
        System.out.println("Needs review: " + needsReview);
    }
}
