import java.util.Locale;
import java.util.Scanner;

public class Exercise02 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        int accepted = 0;
        int skipped = 0;
        int total = 0;

        while (scanner.hasNextLine()) {
            String line = scanner.nextLine().trim();
            if (line.isEmpty()) {
                continue;
            }

            String[] parts = line.split("\\s+");
            if (parts.length != 2) {
                skipped++;
                continue;
            }

            try {
                int score = Integer.parseInt(parts[1]);
                if (score < 0 || score > 100) {
                    skipped++;
                    continue;
                }
                accepted++;
                total += score;
            } catch (NumberFormatException error) {
                skipped++;
            }
        }

        System.out.println("Accepted rows: " + accepted);
        System.out.println("Skipped rows: " + skipped);
        System.out.printf("Average: %.2f%n", accepted == 0 ? 0.0 : (double) total / accepted);
    }
}
