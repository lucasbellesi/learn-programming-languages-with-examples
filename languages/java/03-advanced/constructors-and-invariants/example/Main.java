// Module focus: Building objects that start valid and stay valid through guarded updates.
// Why it matters: practicing constructors and invariants patterns makes exercises and checkpoints easier to reason about.

import java.util.Locale;

public class Main {
    static class Temperature {
        private double celsius;

        Temperature(double celsiusValue) {
            // The constructor clamps invalid starting data so every object starts valid.
            celsius = Math.max(-273.15, celsiusValue);
        }

        boolean setCelsius(double newValue) {
            // Updates must protect the same invariant as construction.
            if (newValue < -273.15) {
                return false;
            }

            celsius = newValue;
            return true;
        }

        double celsius() {
            // Accessors expose the valid state without letting callers edit fields directly.
            return celsius;
        }
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        // Prepare sample inputs that exercise the key constructors and invariants path.
        Temperature temperature = new Temperature(-500.0);

        // Report values so learners can verify the constructors and invariants outcome.
        System.out.printf("Initial value (clamped): %.2f C%n", temperature.celsius());

        boolean updated = temperature.setCelsius(25.0);
        System.out.println("Set to 25.0 success: " + updated);
        System.out.printf("Current value: %.2f C%n", temperature.celsius());

        boolean rejected = temperature.setCelsius(-300.0);
        System.out.println("Set to -300.0 success: " + rejected);

        System.out.printf("Current value: %.2f C%n", temperature.celsius());
    }
}
