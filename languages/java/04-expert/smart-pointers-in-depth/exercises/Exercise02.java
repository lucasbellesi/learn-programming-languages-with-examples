import java.util.Scanner;

public class Exercise02 {
    private static void runSmartPointersInDepthExercise() {
        Scanner scanner = new Scanner(System.in);
        String scenario = scanner.hasNextLine() ? scanner.nextLine() : "missing";
        // TODO 1: Accept `alive`, `expired`, or `missing` as the lookup scenario.
        // TODO 2: Observe cache entries through `WeakReference`.
        // TODO 3: Produce alive/expired cache lookup logs; verify expired weak reference; cache miss.
        if (scenario.isEmpty()) {
            return;
        }
    }

    public static void main(String[] args) {
        runSmartPointersInDepthExercise();
    }
}
