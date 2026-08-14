import java.util.Locale;
import java.util.Scanner;

public class Exercise02 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        double principal = scanner.nextDouble();
        double rate = scanner.nextDouble();
        int years = scanner.nextInt();
        double interest = principal * rate * years;
        System.out.printf("Principal: %.2f%n", principal);
        System.out.printf("Interest: %.2f%n", interest);
        System.out.printf("Final amount: %.2f%n", principal + interest);
    }
}
