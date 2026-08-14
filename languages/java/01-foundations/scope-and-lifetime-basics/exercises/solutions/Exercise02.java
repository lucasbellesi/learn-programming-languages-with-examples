import java.util.Scanner;

public class Exercise02 {
    static int calls = 0;

    static void recordCall() {
        calls++;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        for (int i = 0; i < count; i++) {
            recordCall();
        }
        System.out.println("Calls recorded: " + calls);
    }
}
