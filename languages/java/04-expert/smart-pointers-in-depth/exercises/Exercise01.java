import java.util.Scanner;

public class Exercise01 {
    private static void runSmartPointersInDepthExercise() {
        Scanner scanner = new Scanner(System.in);
        String sourceName = scanner.hasNextLine() ? scanner.nextLine() : "empty";
        String destinationName = scanner.hasNextLine() ? scanner.nextLine() : "empty";
        // TODO 1: Convert `empty` to a null holder and other lines to owned documents.
        // TODO 2: Move an owned document reference between holders.
        // TODO 3: Produce ownership transfer logs before and after moving; verify moving from an empty
        //         owner; destination already holding another object.
        if (sourceName.isEmpty() && destinationName.isEmpty()) {
            return;
        }
    }

    public static void main(String[] args) {
        runSmartPointersInDepthExercise();
    }
}
