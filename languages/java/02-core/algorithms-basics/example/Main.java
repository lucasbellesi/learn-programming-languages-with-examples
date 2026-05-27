// Module focus: Walking data step by step to compute summaries and decisions.
// Why it matters: practicing algorithms basics patterns makes exercises and checkpoints easier to reason about.

public class Main {
    static int firstIndexOf(int[] values, int target) {
        for (int i = 0; i < values.length; i++) {
            if (values[i] == target) {
                // Return immediately because the first match is the result this helper promises.
                return i;
            }
        }
        return -1;
    }

    static int countOccurrences(int[] values, int target) {
        int count = 0;
        for (int value : values) {
            // Counting does not stop at the first match; every element still matters.
            if (value == target) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int[] values = {4, 7, 4, 2, 4, 9};
        int target = 4;

        // Report both position and frequency so learners can compare related scans.
        System.out.println("First index of 4: " + firstIndexOf(values, target));
        System.out.println("Occurrences of 4: " + countOccurrences(values, target));
    }
}
