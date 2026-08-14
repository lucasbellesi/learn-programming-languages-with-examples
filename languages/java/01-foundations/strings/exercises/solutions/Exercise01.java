import java.util.Scanner;

public class Exercise01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String raw = scanner.nextLine();
        String cleaned = raw.trim();
        System.out.println("Cleaned: " + cleaned);
        System.out.println("Lowercase: " + cleaned.toLowerCase());
        System.out.println("Length: " + cleaned.length());
    }
}
