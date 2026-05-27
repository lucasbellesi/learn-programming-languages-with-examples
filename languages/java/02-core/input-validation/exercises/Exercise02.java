import java.util.Locale;
import java.util.Scanner;

public class Exercise02 {
    static Integer readInt(Scanner scanner) {
        while (scanner.hasNext()) {
            String token = scanner.next();
            try {
                return Integer.parseInt(token);
            } catch (NumberFormatException error) {
                System.out.println("Invalid integer.");
            }
        }
        return null;
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);

        Integer count = null;
        while (scanner.hasNext() && count == null) {
            Integer candidate = readInt(scanner);
            if (candidate == null) {
                break;
            }
            if (candidate < 1 || candidate > 50) {
                System.out.println("Count must be 1..50.");
            } else {
                count = candidate;
            }
        }

        if (count == null) {
            System.out.println("No valid count provided.");
            return;
        }

        int accepted = 0;
        int total = 0;
        while (accepted < count && scanner.hasNext()) {
            Integer score = readInt(scanner);
            if (score == null) {
                break;
            }
            if (score < 0 || score > 100) {
                System.out.println("Score must be 0..100.");
                continue;
            }
            total += score;
            accepted++;
        }

        if (accepted < count) {
            System.out.println("Not enough valid scores.");
            return;
        }

        System.out.printf("Average score: %.2f%n", (double) total / count);
    }
}
