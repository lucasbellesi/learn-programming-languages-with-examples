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

    static String readNonEmpty(Scanner scanner, String prompt) {
        while (true) {
            System.out.print(prompt);
            String value = scanner.nextLine().trim();
            if (!value.isEmpty()) {
                return value;
            }
            System.out.println("This value cannot be empty.");
        }
    }

    static int readScore(Scanner scanner, String prompt) {
        while (true) {
            System.out.print(prompt);
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
        List<Student> students = new ArrayList<>();
        int count = readPositiveCount(scanner);

        for (int index = 1; index <= count; index++) {
            String name = readNonEmpty(scanner, "Student #" + index + " name: ");
            int score = readScore(scanner, name + "'s score (0-100): ");
            students.add(new Student(name, score));
        }

        int total = 0;
        Student highest = students.get(0);
        Student lowest = students.get(0);
        int passed = 0;

        System.out.println("Students:");
        for (Student student : students) {
            System.out.println("- " + student.name() + ": " + student.score());
            total += student.score();
            if (student.score() > highest.score()) {
                highest = student;
            }
            if (student.score() < lowest.score()) {
                lowest = student;
            }
            if (student.score() >= 60) {
                passed++;
            }
        }

        System.out.printf("Average: %.2f%n", (double) total / students.size());
        System.out.println("Highest: " + highest.name() + " (" + highest.score() + ")");
        System.out.println("Lowest: " + lowest.name() + " (" + lowest.score() + ")");
        System.out.println("Passed: " + passed + "/" + students.size());
    }
}
