// Module focus: Reordering data and locating values with deliberate search logic.
// Why it matters: practicing sorting and searching patterns makes exercises and checkpoints easier to reason about.

import java.util.Arrays;

public class Main {
    static int indexOf(int[] values, int target) {
        for (int i = 0; i < values.length; i++) {
            if (values[i] == target) {
                // The sorted index is returned as soon as the target appears.
                return i;
            }
        }
        return -1;
    }

    static String joinValues(int[] values) {
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < values.length; i++) {
            // Manual joining keeps the output format identical to the contract.
            if (i > 0) {
                builder.append(" ");
            }
            builder.append(values[i]);
        }
        return builder.toString();
    }

    public static void main(String[] args) {
        int[] scores = {91, 77, 64, 95, 77, 88};
        // Sorting mutates this array, which is fine because the original order is no longer needed.
        Arrays.sort(scores);

        // Report the sorted data and search outcomes so the order is visible.
        System.out.println("Sorted: " + joinValues(scores));
        System.out.println("Index of 88: " + indexOf(scores, 88));
        System.out.println("Index of 70: " + indexOf(scores, 70));
    }
}
