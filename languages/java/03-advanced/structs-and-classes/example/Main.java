// Module focus: Modeling related data and behavior with structured types.
// Why it matters: practicing structs and classes patterns makes exercises and checkpoints easier to reason about.

import java.util.List;
import java.util.Locale;

public class Main {
    record Coordinate(int x, int y) {
        int manhattanDistanceFromOrigin() {
            // Records are a good fit for small immutable values with derived behavior.
            return Math.abs(x) + Math.abs(y);
        }
    }

    static class Wallet {
        private final String owner;
        private double balance;

        Wallet(String owner, double initialBalance) {
            // Constructors are the first chance to normalize or reject invalid state.
            String cleanOwner = owner == null ? "" : owner.trim();
            this.owner = cleanOwner.isEmpty() ? "Unknown" : cleanOwner;
            this.balance = Math.max(0.0, initialBalance);
        }

        boolean deposit(double amount) {
            // Invalid deposits are rejected instead of silently changing state.
            if (amount <= 0.0) {
                return false;
            }
            balance += amount;
            return true;
        }

        boolean withdraw(double amount) {
            // Methods protect the balance invariant by rejecting impossible updates.
            if (amount <= 0.0 || amount > balance) {
                return false;
            }
            balance -= amount;
            return true;
        }

        String owner() {
            // Accessor methods expose read-only views of private fields.
            return owner;
        }

        double balance() {
            return balance;
        }
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        // Prepare sample inputs that exercise the record path.
        List<Coordinate> route = List.of(new Coordinate(2, 3), new Coordinate(-1, 4), new Coordinate(5, -2));

        // Report values so learners can verify the structs and classes outcome.
        System.out.println("Coordinates (record example):");
        for (Coordinate point : route) {
            System.out.println(
                    "Point (%d, %d), Manhattan distance = %d"
                            .formatted(point.x(), point.y(), point.manhattanDistanceFromOrigin()));
        }

        Wallet wallet = new Wallet("Maya", 120.0);
        // Run controlled mutations through methods rather than editing fields directly.
        wallet.deposit(35.0);
        wallet.withdraw(40.0);

        System.out.println();
        System.out.println("Wallet (class example):");
        System.out.println("Owner: " + wallet.owner());
        System.out.printf("Balance: %.2f%n", wallet.balance());
    }
}
