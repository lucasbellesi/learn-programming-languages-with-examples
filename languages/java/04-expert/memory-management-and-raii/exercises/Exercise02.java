import java.util.Scanner;

public class Exercise02 {
    private static void runMemoryManagementRaiiExercise() {
        Scanner scanner = new Scanner(System.in);
        String depthText = scanner.hasNextLine() ? scanner.nextLine() : "";
        // TODO 1: Validate depthText as a positive number of nested scopes.
        // TODO 2: Scope guard that proves nested cleanup order.
        // TODO 3: Produce enter/close logs proving automatic cleanup; verify nested scopes; final
        //         active counter must return to zero.
        if (depthText.isEmpty()) {
            return;
        }
    }

    public static void main(String[] args) {
        runMemoryManagementRaiiExercise();
    }
}
