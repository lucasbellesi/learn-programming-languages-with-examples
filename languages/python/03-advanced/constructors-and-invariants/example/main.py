# Module focus: Building objects that start valid and stay valid through guarded updates.
# Why it matters: the example makes it possible to construct objects only in valid states
# before the learner tackles the exercises.

# Separate helpers keep the main path focused on how to construct objects only in valid states.
class Temperature:
    def __init__(self, celsius_value: float) -> None:
        # These values exercise the normal path before the exercises vary the documented
        # boundaries.
        self._celsius = max(-273.15, celsius_value)

    def set_celsius(self, new_value: float) -> bool:
        if new_value < -273.15:
            return False

        self._celsius = new_value
        return True

    @property
    def celsius(self) -> float:
        return self._celsius


# Fixed inputs make the consequence of accepting invalid constructor values and fixing later
# visible and repeatable.
def main() -> None:
    temperature = Temperature(-500.0)
    # The printed result shows whether the program can keep mutations from violating established
    # invariants.
    print(f"Initial value (clamped): {temperature.celsius:.2f} C")

    updated = temperature.set_celsius(25.0)
    print(f"Set to 25.0 success: {updated}")
    print(f"Current value: {temperature.celsius:.2f} C")

    rejected = temperature.set_celsius(-300.0)
    print(f"Set to -300.0 success: {rejected}")

    print(f"Current value: {temperature.celsius:.2f} C")


if __name__ == "__main__":
    main()
