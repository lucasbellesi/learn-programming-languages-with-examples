// Module focus: Reusing command operations through a small registry boundary.
// Why it matters: callers can dispatch behavior without owning every implementation detail.

import java.util.Map;
import java.util.OptionalInt;
import java.util.Scanner;

public class Exercise02 {
    @FunctionalInterface
    interface Operation {
        OptionalInt apply(int left, int right);
    }

    public static void main(String[] args) {
        Map<String, Operation> operations = Map.of(
                "add", (left, right) -> OptionalInt.of(left + right),
                "mul", (left, right) -> OptionalInt.of(left * right),
                "div", (left, right) -> right == 0
                        ? OptionalInt.empty()
                        : OptionalInt.of(left / right));

        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNext()) {
            System.out.println("Invalid command.");
            return;
        }
        String command = scanner.next().toLowerCase();

        if (!scanner.hasNextInt()) {
            System.out.println("Invalid left operand.");
            return;
        }
        int left = scanner.nextInt();

        if (!scanner.hasNextInt()) {
            System.out.println("Invalid right operand.");
            return;
        }
        int right = scanner.nextInt();

        Operation operation = operations.get(command);
        if (operation == null) {
            System.out.println("Unsupported command.");
            return;
        }

        OptionalInt result = operation.apply(left, right);
        if (result.isEmpty()) {
            System.out.println("Operation failed.");
            return;
        }

        System.out.println("Operation: " + command);
        System.out.println("Result: " + result.getAsInt());
    }
}
