import java.util.Scanner;

public class Exercise02 {
    static class SimpleDate {
        private static final int[] DAYS_IN_MONTH = {
            31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
        };

        private final int month;
        private final int day;

        SimpleDate(int month, int day) {
            this.month = month;
            this.day = day;
        }

        boolean isValid() {
            if (month < 1 || month > 12) {
                return false;
            }
            return day >= 1 && day <= DAYS_IN_MONTH[month - 1];
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            System.out.println("Invalid input.");
            return;
        }
        int month = scanner.nextInt();

        if (!scanner.hasNextInt()) {
            System.out.println("Invalid input.");
            return;
        }
        int day = scanner.nextInt();

        SimpleDate date = new SimpleDate(month, day);
        System.out.println(date.isValid() ? "Valid date" : "Invalid date");
    }
}
