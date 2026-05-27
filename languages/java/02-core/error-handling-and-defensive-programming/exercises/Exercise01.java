import java.util.Scanner;

public class Exercise01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            int left = Integer.parseInt(scanner.next());
            int right = Integer.parseInt(scanner.next());
            if (right == 0) {
                System.out.println("Cannot divide by zero.");
                return;
            }
            System.out.println("Result: " + (left / right));
        } catch (RuntimeException error) {
            System.out.println("Invalid integer input.");
        }
    }
}
