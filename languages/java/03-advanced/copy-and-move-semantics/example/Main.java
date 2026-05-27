// Module focus: How copying, sharing, or transferring state changes later behavior.
// Why it matters: practicing copy and move semantics patterns makes exercises and checkpoints easier to reason about.

import java.util.ArrayList;
import java.util.List;

public class Main {
    static final class InventoryRecord {
        private final String name;
        private final List<Integer> counts;

        InventoryRecord(String name, List<Integer> counts) {
            this.name = name;
            this.counts = new ArrayList<>(counts);
        }

        static InventoryRecord shallowFrom(InventoryRecord source) {
            // This bypasses the public constructor to demonstrate shared nested state.
            return new InventoryRecord(source.name, source.counts, false);
        }

        InventoryRecord defensiveCopy() {
            // The public constructor copies the list, so later updates cannot leak back.
            return new InventoryRecord(name, counts);
        }

        private InventoryRecord(String name, List<Integer> counts, boolean copyCounts) {
            this.name = name;
            this.counts = copyCounts ? new ArrayList<>(counts) : counts;
        }

        void adjustStock(int delta) {
            counts.set(0, counts.get(0) + delta);
        }

        void adjustReserved(int delta) {
            counts.set(1, counts.get(1) + delta);
        }

        String summary() {
            return counts.get(0) + "/" + counts.get(1);
        }

        List<Integer> snapshot() {
            // Immutable snapshots let callers inspect state without mutating internals.
            return List.copyOf(counts);
        }
    }

    public static void main(String[] args) {
        InventoryRecord original = new InventoryRecord("Keyboard", List.of(10, 2));

        // These three names model aliasing, shallow copying, and defensive copying side by side.
        InventoryRecord alias = original;
        InventoryRecord shallowCopy = InventoryRecord.shallowFrom(original);
        InventoryRecord defensiveCopy = original.defensiveCopy();

        // Mutating each reference reveals which objects still share nested state.
        alias.adjustStock(-1);
        shallowCopy.adjustReserved(3);
        defensiveCopy.adjustStock(5);

        // Report output values so learners can verify the copy and move semantics result.
        System.out.println("Original: " + original.summary());
        System.out.println("Shallow copy: " + shallowCopy.summary());
        System.out.println("Defensive copy: " + defensiveCopy.summary());
        System.out.println("Snapshot size: " + original.snapshot().size());
    }
}
