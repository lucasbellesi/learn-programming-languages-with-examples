import java.util.Scanner;

public class Exercise01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNext()) {
            String token = scanner.next();
            try {
                int value = Integer.parseInt(token);
                if (value < 1 || value > 100) {
                    System.out.println("Out of range.");
                    continue;
                }
                System.out.println("Accepted: " + value);
                System.out.println("Square: " + (value * value));
                return;
            } catch (NumberFormatException error) {
                System.out.println("Invalid integer.");
            }
        }

        System.out.println("No valid value provided.");
    }
}
