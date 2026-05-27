// Module focus: Counting repeated values and summarizing them through keyed lookups.
// Why it matters: practicing maps and frequency counting patterns makes exercises and checkpoints easier to reason about.

import java.util.Locale;
import java.util.Map;
import java.util.TreeMap;

public class Main {
    public static void main(String[] args) {
        String text = "learn java learn maps";
        Map<String, Integer> frequencies = new TreeMap<>();

        // Normalize each token before counting so equivalent words share one key.
        for (String word : text.toLowerCase(Locale.US).split("\\s+")) {
            frequencies.put(word, frequencies.getOrDefault(word, 0) + 1);
        }

        // Report sorted frequencies to keep the output stable across runs.
        System.out.println("Word frequencies:");
        for (Map.Entry<String, Integer> entry : frequencies.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }
    }
}
