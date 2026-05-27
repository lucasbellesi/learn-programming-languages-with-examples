// Module focus: Guarding risky inputs so failures stay explicit and controlled.
// Why it matters: practicing error handling and defensive programming patterns makes exercises and checkpoints easier to reason about.

public class Main {
    static int divide(int left, int right) {
        if (right == 0) {
            // Guard before the risky operation so the failure has a clear explanation.
            throw new ArithmeticException("division by zero");
        }
        return left / right;
    }

    public static void main(String[] args) {
        String[] rows = {"42 6", "18 0", "bad row"};

        for (String row : rows) {
            try {
                String[] parts = row.split("\\s+");
                // Parsing is intentionally inside the try block because malformed rows are expected.
                int left = Integer.parseInt(parts[0]);
                int right = Integer.parseInt(parts[1]);

                // Report valid calculations and recoverable failures from the same loop.
                System.out.println("Input: " + left + " " + right);
                System.out.println("Result: " + divide(left, right));
            } catch (ArithmeticException error) {
                System.out.println("Cannot divide by zero.");
            } catch (RuntimeException error) {
                // Other runtime failures are treated as malformed input rows for this exercise.
                System.out.println("Skipped invalid row: " + row);
            }
        }
    }
}
