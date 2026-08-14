// Module focus: Comparing string-building strategies on the same repeated workload.
// Why it matters: validation and repeated measurements are stronger evidence than one timing.

import java.util.Scanner;
import java.util.function.Supplier;

public class Exercise01 {
    private static final int RUNS = 5;
    private static volatile int lengthSink;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            System.out.println("Invalid fragment count.");
            return;
        }

        int fragmentCount = scanner.nextInt();
        if (fragmentCount < 0) {
            System.out.println("Fragment count cannot be negative.");
            return;
        }

        Supplier<String> concatenation = () -> buildWithConcatenation(fragmentCount);
        Supplier<String> builder = () -> buildWithBuilder(fragmentCount);
        String concatenated = concatenation.get();
        String buffered = builder.get();

        long concatenationAverage = measureAverageNanos(concatenation);
        long builderAverage = measureAverageNanos(builder);

        System.out.println("Outputs equal: " + concatenated.equals(buffered));
        System.out.println("Output length: " + concatenated.length());
        System.out.println("Concatenation average ns: " + concatenationAverage);
        System.out.println("StringBuilder average ns: " + builderAverage);
    }

    private static String buildWithConcatenation(int fragmentCount) {
        String result = "";
        for (int index = 0; index < fragmentCount; index++) {
            result += "item-" + index + ";";
        }
        return result;
    }

    private static String buildWithBuilder(int fragmentCount) {
        StringBuilder builder = new StringBuilder(fragmentCount * 10);
        for (int index = 0; index < fragmentCount; index++) {
            builder.append("item-").append(index).append(';');
        }
        return builder.toString();
    }

    private static long measureAverageNanos(Supplier<String> action) {
        lengthSink = action.get().length();
        long total = 0;
        for (int iteration = 0; iteration < RUNS; iteration++) {
            long started = System.nanoTime();
            lengthSink = action.get().length();
            total += System.nanoTime() - started;
        }
        return total / RUNS;
    }
}
