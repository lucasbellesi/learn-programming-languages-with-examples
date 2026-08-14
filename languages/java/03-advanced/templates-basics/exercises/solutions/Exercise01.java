// Module focus: Building a small generic class that preserves the caller's type.
// Why it matters: generic containers are the foundation of many Java standard-library APIs.

import java.util.Scanner;

public class Exercise01 {
    static final class Pair<T> {
        private final T first;
        private final T second;

        Pair(T first, T second) {
            this.first = first;
            this.second = second;
        }

        Pair<T> swapped() {
            // The returned pair keeps the same type parameter as the original pair.
            return new Pair<>(second, first);
        }

        String describe() {
            return first + " " + second;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNext()) {
            System.out.println("Missing first value.");
            return;
        }
        String first = scanner.next();

        if (!scanner.hasNext()) {
            System.out.println("Missing second value.");
            return;
        }
        String second = scanner.next();

        Pair<String> pair = new Pair<>(first, second);
        Pair<String> swapped = pair.swapped();

        System.out.println("Before: " + pair.describe());
        System.out.println("After: " + swapped.describe());
    }
}
