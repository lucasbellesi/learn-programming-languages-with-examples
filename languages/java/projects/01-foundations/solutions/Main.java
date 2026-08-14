import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    record Student(String name, int score) {
    }

    static int readPositiveCount(Scanner scanner) {
        while (true) {
            System.out.print("How many students? ");
            String raw = scanner.nextLine().trim();
            try {
                int value = Integer.parseInt(raw);
                if (value > 0) {
                    return value;
                }
                System.out.println("Please enter a number greater than zero.");
            } catch (NumberFormatException error) {
                System.out.println("Please enter a valid integer.");
            }
        }
    }

    static String readName(Scanner scanner, int index) {
        while (true) {
            System.out.print("Student #" + index + " name: ");
            String name = scanner.nextLine().trim();
            if (!name.isEmpty()) {
                return name;
            }
            System.out.println("Name cannot be empty.");
        }
    }

    static int readScore(Scanner scanner, String name) {
        while (true) {
            System.out.print(name + "'s score (0-100): ");
            String raw = scanner.nextLine().trim();
            try {
                int score = Integer.parseInt(raw);
                if (score >= 0 && score <= 100) {
                    return score;
                }
                System.out.println("Score must be between 0 and 100.");
            } catch (NumberFormatException error) {
                System.out.println("Please enter a valid integer score.");
            }
        }
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        int totalStudents = readPositiveCount(scanner);
        List<Student> students = new ArrayList<>();

        for (int index = 1; index <= totalStudents; index++) {
            String name = readName(scanner, index);
            int score = readScore(scanner, name);
            students.add(new Student(name, score));
        }

        int total = 0;
        int minimum = students.get(0).score();
        int maximum = students.get(0).score();

        System.out.println("Students:");
        for (Student student : students) {
            System.out.println("- " + student.name() + ": " + student.score());
            total += student.score();
            minimum = Math.min(minimum, student.score());
            maximum = Math.max(maximum, student.score());
        }

        double average = (double) total / students.size();
        System.out.printf("Average: %.2f%n", average);
        System.out.println("Minimum: " + minimum);
        System.out.println("Maximum: " + maximum);
    }
}
