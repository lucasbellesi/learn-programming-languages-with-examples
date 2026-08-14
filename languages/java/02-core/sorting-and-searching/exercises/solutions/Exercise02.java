import java.util.Arrays;
import java.util.Scanner;

public class Exercise02 {
    static int indexOf(int[] values, int target) {
        for (int i = 0; i < values.length; i++) {
            if (values[i] == target) {
                return i;
            }
        }
        return -1;
    }

    static String joinValues(int[] values) {
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < values.length; i++) {
            if (i > 0) {
                builder.append(" ");
            }
            builder.append(values[i]);
        }
        return builder.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        int[] values = new int[count];
        for (int i = 0; i < count; i++) {
            values[i] = scanner.nextInt();
        }
        int target = scanner.nextInt();

        Arrays.sort(values);
        System.out.println("Sorted: " + joinValues(values));
        System.out.println("Found " + target + " at index " + indexOf(values, target));
    }
}
