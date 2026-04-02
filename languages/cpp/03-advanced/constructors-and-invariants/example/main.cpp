// This example shows building objects that start valid and stay valid through guarded updates.
// In C++, the example keeps value flow, references, and explicit control visible.

#include <iostream>
#include <string>
using namespace std;

class Temperature {
  public:
    explicit Temperature(double celsiusValue) : celsius(celsiusValue) {
        if (celsius < -273.15) {
            celsius = -273.15;
        }
    }

    bool setCelsius(double newValue) {
        if (newValue < -273.15) {
            return false;
        }
        celsius = newValue;
        return true;
    }

    double getCelsius() const { return celsius; }

  private:
    double celsius;
};

// Run one deterministic scenario so the console output makes building objects that start valid and
// stay valid through guarded updates easy to verify.
int main() {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    Temperature temp(-500.0);
    // Print the observed state here so learners can connect the code path to a concrete result.
    cout << "Initial value (clamped): " << temp.getCelsius() << " C\n";

    const bool ok = temp.setCelsius(25.0);
    cout << "Set to 25.0 success: " << (ok ? "true" : "false") << '\n';
    cout << "Current value: " << temp.getCelsius() << " C\n";

    const bool invalid = temp.setCelsius(-300.0);
    cout << "Set to -300.0 success: " << (invalid ? "true" : "false") << '\n';
    cout << "Current value: " << temp.getCelsius() << " C\n";

    return 0;
}
