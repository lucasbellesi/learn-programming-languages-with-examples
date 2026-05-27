import java.util.Locale;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class Exercise01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String line = scanner.hasNextLine() ? scanner.nextLine() : "";
        Map<String, Integer> frequencies = new TreeMap<>();

        for (String rawWord : line.toLowerCase(Locale.US).split("\\s+")) {
            if (rawWord.isBlank()) {
                continue;
            }
            frequencies.put(rawWord, frequencies.getOrDefault(rawWord, 0) + 1);
        }

        System.out.println("Word frequencies:");
        for (Map.Entry<String, Integer> entry : frequencies.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
