import java.util.Scanner;

public class Exercise02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        if (count <= 0) {
            System.out.println("Count must be positive.");
            return;
        }

        int minimum = Integer.MAX_VALUE;
        int maximum = Integer.MIN_VALUE;
        int evenCount = 0;
        for (int i = 0; i < count; i++) {
            int value = scanner.nextInt();
            minimum = Math.min(minimum, value);
            maximum = Math.max(maximum, value);
            if (value % 2 == 0) {
                evenCount++;
            }
        }

        System.out.println("Minimum: " + minimum);
        System.out.println("Maximum: " + maximum);
        System.out.println("Even numbers: " + evenCount);
    }
}
