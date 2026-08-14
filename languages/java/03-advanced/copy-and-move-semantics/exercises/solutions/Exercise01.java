// Module focus: Separating cloned state from transfer-style state handoff.
// Why it matters: Java references make it important to choose when state is shared and when it is copied.

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Exercise01 {
    static final class Buffer {
        private List<Integer> values;

        Buffer(int size) {
            if (size < 0) {
                size = 0;
            }
            values = new ArrayList<>();
            for (int index = 0; index < size; index++) {
                values.add(index + 1);
            }
        }

        private Buffer(List<Integer> values) {
            this.values = values;
        }

        Buffer cloneBuffer() {
            // Cloning creates independent storage with the same values.
            return new Buffer(new ArrayList<>(values));
        }

        Buffer transfer() {
            List<Integer> transferred = values;
            values = new ArrayList<>();
            return new Buffer(transferred);
        }

        int size() {
            return values.size();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            System.out.println("Invalid size.");
            return;
        }

        Buffer first = new Buffer(scanner.nextInt());
        Buffer second = first.cloneBuffer();
        Buffer third = second.transfer();

        System.out.println("first size: " + first.size());
        System.out.println("second size (after transfer): " + second.size());
        System.out.println("third size: " + third.size());
    }
}
