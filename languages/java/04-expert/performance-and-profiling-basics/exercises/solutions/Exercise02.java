// Module focus: Measuring list growth with and without a known initial capacity.
// Why it matters: equal checksums prove both measured paths performed equivalent work.

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.function.Supplier;

public class Exercise02 {
    private static final int RUNS = 8;
    private static volatile long checksumSink;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            System.out.println("Invalid element count.");
            return;
        }

        int elementCount = scanner.nextInt();
        if (elementCount < 0) {
            System.out.println("Element count cannot be negative.");
            return;
        }

        Supplier<List<Integer>> withoutCapacity = () -> fillValues(elementCount, false);
        Supplier<List<Integer>> withCapacity = () -> fillValues(elementCount, true);
        long firstChecksum = checksum(withoutCapacity.get());
        long secondChecksum = checksum(withCapacity.get());

        long withoutCapacityAverage = measureAverageNanos(withoutCapacity);
        long withCapacityAverage = measureAverageNanos(withCapacity);

        System.out.println("Checksums equal: " + (firstChecksum == secondChecksum));
        System.out.println("Checksum: " + firstChecksum);
        System.out.println("Without capacity average ns: " + withoutCapacityAverage);
        System.out.println("With capacity average ns: " + withCapacityAverage);
    }

    private static List<Integer> fillValues(int elementCount, boolean reserveCapacity) {
        List<Integer> values = reserveCapacity
                ? new ArrayList<>(elementCount)
                : new ArrayList<>();
        for (int index = 0; index < elementCount; index++) {
            values.add(index);
        }
        return values;
    }

    private static long checksum(List<Integer> values) {
        long total = 0;
        for (int value : values) {
            total += value;
        }
        return total;
    }

    private static long measureAverageNanos(Supplier<List<Integer>> action) {
        checksumSink = checksum(action.get());
        long total = 0;
        for (int iteration = 0; iteration < RUNS; iteration++) {
            long started = System.nanoTime();
            checksumSink = checksum(action.get());
            total += System.nanoTime() - started;
        }
        return total / RUNS;
    }
}
