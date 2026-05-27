// Module focus: Tying resource cleanup to object lifetime so cleanup stays predictable.
// Why it matters: practicing memory management and raii patterns makes exercises and checkpoints easier to reason about.

import java.util.Arrays;

public class Main {
    static final class BufferLease implements AutoCloseable {
        private static int activeLeases = 0;

        private final String name;
        private int[] values;
        private boolean closed;

        BufferLease(String name, int size) {
            this.name = name;
            this.values = new int[Math.max(0, size)];
            // Acquisition updates shared state immediately so cleanup can be verified later.
            activeLeases++;
            System.out.printf("[acquire] %s size=%d active=%d%n", name, values.length, activeLeases);
        }

        static int activeLeases() {
            return activeLeases;
        }

        void fillSequence(int start, int step) {
            ensureOpen();
            for (int index = 0; index < values.length; index++) {
                values[index] = start + (index * step);
            }
        }

        int total() {
            ensureOpen();
            int sum = 0;
            // Summing through the live resource proves methods are guarded before close.
            for (int value : values) {
                sum += value;
            }
            return sum;
        }

        String describe() {
            ensureOpen();
            return Arrays.toString(values);
        }

        @Override
        public void close() {
            // Idempotent close keeps cleanup safe if callers close manually before scope exit.
            if (closed) {
                return;
            }
            closed = true;
            // Releasing the backing storage makes accidental reuse visible during testing.
            values = new int[0];
            activeLeases--;
            System.out.printf("[close] %s active=%d%n", name, activeLeases);
        }

        private void ensureOpen() {
            if (closed) {
                throw new IllegalStateException("buffer already closed");
            }
        }
    }

    public static void main(String[] args) {
        // Report values so learners can verify the memory management and raii outcome.
        System.out.println("Active before scope: " + BufferLease.activeLeases());

        // try-with-resources closes resources automatically at the end of this block.
        try (BufferLease scores = new BufferLease("scores", 5)) {
            scores.fillSequence(10, 5);
            System.out.println("Scores: " + scores.describe());
            System.out.println("Sum: " + scores.total());

            // Nested resources close in reverse order, just like stacked scope cleanup.
            try (BufferLease scratch = new BufferLease("scratch", 3)) {
                scratch.fillSequence(1, 1);
                System.out.println("Scratch: " + scratch.describe());
                System.out.println("Active inside scope: " + BufferLease.activeLeases());
            }
        }

        System.out.println("Active after scope: " + BufferLease.activeLeases());
    }
}
