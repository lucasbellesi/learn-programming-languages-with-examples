// Module focus: Storing related values in ordered collections and iterating safely.
// Why it matters: practicing arrays and vectors patterns makes exercises and checkpoints easier to reason about.

public class Main {
    public static void main(String[] args) {
        int[] scores = {91, 77, 88, 77};
        int total = 0;
        int matches = 0;

        // A for-each loop is a safe first pass when the index itself is not needed.
        for (int score : scores) {
            total += score;
            if (score == 77) {
                matches++;
            }
        }

        // Report the collection size, aggregate, and match count as observable checks.
        System.out.println("Scores: " + scores.length);
        System.out.println("Total: " + total);
        System.out.println("Scores equal to 77: " + matches);
    }
}
