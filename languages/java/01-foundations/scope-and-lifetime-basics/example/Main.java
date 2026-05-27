// Module focus: How names stay visible only inside the blocks that own them.
// Why it matters: practicing scope and lifetime basics patterns makes exercises and checkpoints easier to reason about.

public class Main {
    static int calls = 0;

    static int nextScore(int score) {
        calls++;
        int bonus = 5;
        return score + bonus;
    }

    public static void main(String[] args) {
        int score = 80;

        // The helper's local bonus is gone after the method returns; only the result remains.
        int adjusted = nextScore(score);

        // Report values from different scopes without exposing the helper's local variable.
        System.out.println("Original: " + score);
        System.out.println("Adjusted: " + adjusted);
        System.out.println("Calls: " + calls);
    }
}
