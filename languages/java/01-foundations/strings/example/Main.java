// Module focus: Cleaning and combining text while preserving readable string logic.
// Why it matters: practicing strings patterns makes exercises and checkpoints easier to reason about.

public class Main {
    public static void main(String[] args) {
        String rawName = "  Ana Maria  ";
        String city = "Buenos Aires";

        // Strings are immutable, so each transformation returns a new value.
        String cleanedName = rawName.trim();
        String slug = cleanedName.toLowerCase().replace(" ", "-");

        // Report the cleaned strings so each transformation has visible evidence.
        System.out.println("Name: " + cleanedName);
        System.out.println("City: " + city);
        System.out.println("Slug: " + slug);
    }
}
