// Module focus: Measuring hot paths before changing code for speed.
// Why it matters: the example makes it possible to measure before optimizing and interpret timing
// data cautiously before the learner tackles the exercises.

import java.util.HashSet;
import java.util.Set;
import java.util.function.IntSupplier;
import java.util.stream.IntStream;

public class Main {
    private static final int MEASURED_RUNS = 8;
    // A volatile sink keeps every measured result observable outside the timed method.
    private static volatile int resultSink;

    public static void main(String[] args) {
        // Build both data structures before timing so setup is excluded from the comparison.
        int[] values = IntStream.range(0, 50_000).toArray();
        Set<Integer> indexedValues = new HashSet<>(values.length * 2);
        for (int value : values) {
            indexedValues.add(value);
        }

        int target = values[values.length - 1];
        IntSupplier linearWork = () -> repeatedLinearSearch(values, target, 100);
        IntSupplier indexedWork = () -> repeatedSetLookup(indexedValues, target, 100);

        // Warm both paths before measuring so first-use JVM work is less dominant.
        warmUp(linearWork);
        warmUp(indexedWork);

        long linearAverage = measureAverageNanos(linearWork);
        int linearMatches = resultSink;
        long indexedAverage = measureAverageNanos(indexedWork);
        int indexedMatches = resultSink;

        // Report output labels and correctness deterministically even though timings vary.
        System.out.println("Matches agree: " + (linearMatches == indexedMatches));
        System.out.println("Linear search average ns: " + linearAverage);
        System.out.println("HashSet lookup average ns: " + indexedAverage);
        System.out.println("Measured runs: " + MEASURED_RUNS);
    }

    private static int repeatedLinearSearch(int[] values, int target, int repetitions) {
        int matches = 0;
        // Each lookup may scan the full array, making the repeated cost intentionally visible.
        for (int attempt = 0; attempt < repetitions; attempt++) {
            for (int value : values) {
                if (value == target) {
                    matches++;
                    break;
                }
            }
        }
        return matches;
    }

    private static int repeatedSetLookup(Set<Integer> values, int target, int repetitions) {
        int matches = 0;
        // The set pays an indexing cost before measurement to provide direct lookup behavior.
        for (int attempt = 0; attempt < repetitions; attempt++) {
            if (values.contains(target)) {
                matches++;
            }
        }
        return matches;
    }

    private static void warmUp(IntSupplier action) {
        for (int iteration = 0; iteration < 3; iteration++) {
            resultSink = action.getAsInt();
        }
    }

    private static long measureAverageNanos(IntSupplier action) {
        long total = 0;
        // Averaging repeated samples reduces the influence of one scheduling interruption.
        for (int iteration = 0; iteration < MEASURED_RUNS; iteration++) {
            long started = System.nanoTime();
            resultSink = action.getAsInt();
            total += System.nanoTime() - started;
        }
        return total / MEASURED_RUNS;
    }
}
