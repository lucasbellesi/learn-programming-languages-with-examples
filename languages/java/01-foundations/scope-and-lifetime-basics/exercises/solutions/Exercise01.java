import java.util.Scanner;

public class Exercise01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int outer = scanner.nextInt();
        System.out.println("Outer before block: " + outer);
        {
            int inner = outer + 5;
            System.out.println("Inner value: " + inner);
        }
        System.out.println("Outer after block: " + outer);
    }
}
