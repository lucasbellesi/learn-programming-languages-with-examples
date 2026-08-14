import java.util.Scanner;

public class Exercise02 {
    static int minimum(int a, int b, int c) {
        return Math.min(a, Math.min(b, c));
    }

    static int maximum(int a, int b, int c) {
        return Math.max(a, Math.max(b, c));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int first = scanner.nextInt();
        int second = scanner.nextInt();
        int third = scanner.nextInt();
        System.out.println("Minimum: " + minimum(first, second, third));
        System.out.println("Maximum: " + maximum(first, second, third));
    }
}
