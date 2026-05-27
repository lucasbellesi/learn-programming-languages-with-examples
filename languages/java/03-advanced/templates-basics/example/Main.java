// Module focus: Writing generic code that stays useful across multiple data types.
// Why it matters: practicing templates basics patterns makes exercises and checkpoints easier to reason about.

import java.util.List;

public class Main {
    static final class Box<T> {
        private final T value;

        Box(T value) {
            this.value = value;
        }

        String describe(String label) {
            // The class keeps the same logic while preserving the value type chosen by the caller.
            return label + ": " + value;
        }
    }

    static <T> T firstOrDefault(List<T> values, T fallback) {
        // A generic method can reuse one algorithm for strings, numbers, or domain objects.
        return values.isEmpty() ? fallback : values.get(0);
    }

    static <T extends Comparable<T>> T max(List<T> values) {
        if (values.isEmpty()) {
            throw new IllegalArgumentException("values must not be empty");
        }

        T best = values.get(0);
        for (T value : values) {
            // The Comparable bound is what makes compareTo available on T.
            if (value.compareTo(best) > 0) {
                best = value;
            }
        }
        return best;
    }

    public static void main(String[] args) {
        List<Integer> scores = List.of(91, 98, 87);
        List<String> names = List.of("Ana", "Bea", "Chen");

        // Report output values so learners can verify the generics basics result.
        System.out.println("First score: " + firstOrDefault(scores, 0));
        System.out.println("First name: " + firstOrDefault(names, "unknown"));
        System.out.println(new Box<>(42).describe("Box<Integer>"));
        System.out.println(new Box<>("Java").describe("Box<String>"));
        System.out.println("Max score: " + max(scores));
    }
}
