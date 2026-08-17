// Module focus: Building objects that start valid and stay valid through guarded updates.
// Why it matters: the example makes it possible to construct objects only in valid states
// before the learner tackles the exercises.

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

// Fixed inputs make the consequence of leaving objects in invalid states visible and repeatable.
int main() {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    Temperature temp(-500.0);
    // The printed result shows whether the program can keep mutations from violating established
    // invariants.
    cout << "Initial value (clamped): " << temp.getCelsius() << " C\n";

    const bool ok = temp.setCelsius(25.0);
    cout << "Set to 25.0 success: " << (ok ? "true" : "false") << '\n';
    cout << "Current value: " << temp.getCelsius() << " C\n";

    const bool invalid = temp.setCelsius(-300.0);
    cout << "Set to -300.0 success: " << (invalid ? "true" : "false") << '\n';
    cout << "Current value: " << temp.getCelsius() << " C\n";

    return 0;
}
