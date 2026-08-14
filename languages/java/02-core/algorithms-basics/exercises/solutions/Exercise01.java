import java.util.Scanner;

public class Exercise01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        int[] values = new int[count];
        for (int i = 0; i < count; i++) {
            values[i] = scanner.nextInt();
        }
        int target = scanner.nextInt();

        int firstIndex = -1;
        int occurrences = 0;
        for (int i = 0; i < values.length; i++) {
            if (values[i] == target) {
                occurrences++;
                if (firstIndex == -1) {
                    firstIndex = i;
                }
            }
        }

        System.out.println("First index: " + firstIndex);
        System.out.println("Occurrences: " + occurrences);
    }
}
