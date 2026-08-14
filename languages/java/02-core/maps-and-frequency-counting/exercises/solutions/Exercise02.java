import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class Exercise02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        Map<Integer, Integer> frequencies = new TreeMap<>();

        for (int i = 0; i < count; i++) {
            int value = scanner.nextInt();
            frequencies.put(value, frequencies.getOrDefault(value, 0) + 1);
        }

        System.out.println("Number frequencies:");
        for (Map.Entry<Integer, Integer> entry : frequencies.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
