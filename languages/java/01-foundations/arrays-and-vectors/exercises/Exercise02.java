import java.util.Scanner;

public class Exercise02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        int[] values = new int[count];
        for (int i = 0; i < count; i++) {
            values[i] = scanner.nextInt();
        }
        int target = scanner.nextInt();
        int matches = 0;
        for (int value : values) {
            if (value == target) {
                matches++;
            }
        }
        System.out.println("Target: " + target);
        System.out.println("Occurrences: " + matches);
    }
}
