import java.util.Scanner;

public class Exercise02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        int positive = 0;
        int negative = 0;
        int zero = 0;
        for (int i = 0; i < count; i++) {
            int value = scanner.nextInt();
            if (value > 0) {
                positive++;
            } else if (value < 0) {
                negative++;
            } else {
                zero++;
            }
        }
        System.out.println("Positive: " + positive);
        System.out.println("Negative: " + negative);
        System.out.println("Zero: " + zero);
    }
}
