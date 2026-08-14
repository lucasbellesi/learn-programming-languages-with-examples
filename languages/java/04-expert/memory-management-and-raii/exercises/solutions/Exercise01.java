// Module focus: Reading values through a resource that is closed deterministically.
// Why it matters: try-with-resources makes cleanup happen even when the work has branches.

import java.util.Scanner;

public class Exercise01 {
    static final class IntBufferLease implements AutoCloseable {
        private static int activeLeases = 0;

        private int[] values;
        private boolean closed;

        IntBufferLease(int size) {
            values = new int[Math.max(0, size)];
            activeLeases++;
        }

        static int activeLeases() {
            return activeLeases;
        }

        void set(int index, int value) {
            ensureOpen();
            values[index] = value;
        }

        int sum() {
            ensureOpen();
            int total = 0;
            for (int value : values) {
                total += value;
            }
            return total;
        }

        String reversed() {
            ensureOpen();
            StringBuilder builder = new StringBuilder();
            for (int index = values.length - 1; index >= 0; index--) {
                if (builder.length() > 0) {
                    builder.append(' ');
                }
                builder.append(values[index]);
            }
            return builder.toString();
        }

        @Override
        public void close() {
            if (closed) {
                return;
            }
            closed = true;
            values = new int[0];
            activeLeases--;
        }

        private void ensureOpen() {
            if (closed) {
                throw new IllegalStateException("buffer already closed");
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            System.out.println("Invalid count.");
            return;
        }

        int count = scanner.nextInt();
        if (count <= 0) {
            System.out.println("Count must be positive.");
            return;
        }

        try (IntBufferLease buffer = new IntBufferLease(count)) {
            for (int index = 0; index < count; index++) {
                if (!scanner.hasNextInt()) {
                    System.out.println("Invalid value.");
                    return;
                }
                buffer.set(index, scanner.nextInt());
            }

            System.out.println("Sum: " + buffer.sum());
            System.out.println("Reversed: " + buffer.reversed());
        }

        System.out.println("Active after scope: " + IntBufferLease.activeLeases());
    }
}
