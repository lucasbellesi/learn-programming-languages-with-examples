// Module focus: Building objects that start valid and stay valid through guarded updates.
// Why it matters: practicing constructors and invariants patterns makes exercises and checkpoints
// easier to reason about.

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

// Walk through one fixed scenario so constructors and invariants behavior stays repeatable.
int main() {
    // Prepare sample inputs that exercise the key constructors and invariants path.
    Temperature temp(-500.0);
    // Report values so learners can verify the constructors and invariants outcome.
    cout << "Initial value (clamped): " << temp.getCelsius() << " C\n";

    const bool ok = temp.setCelsius(25.0);
    cout << "Set to 25.0 success: " << (ok ? "true" : "false") << '\n';
    cout << "Current value: " << temp.getCelsius() << " C\n";

    const bool invalid = temp.setCelsius(-300.0);
    cout << "Set to -300.0 success: " << (invalid ? "true" : "false") << '\n';
    cout << "Current value: " << temp.getCelsius() << " C\n";

    return 0;
}
