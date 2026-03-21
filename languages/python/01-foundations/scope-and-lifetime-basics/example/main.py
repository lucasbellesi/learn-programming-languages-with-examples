# This example demonstrates scope and lifetime basics concepts.
# Example purpose: show the module flow with clear, beginner-friendly steps.

PASSING_SCORE = 60


def classify(score):
    # Intent: guard invalid or edge-case paths before the main path continues.
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= PASSING_SCORE:
        return "D"
    return "F"


# Intent: gather typed input first so later operations are predictable.
value = int(input("Enter score: "))
grade = classify(value)

# Intent: print intermediate or final output for quick behavior verification.
print(f"Grade: {grade}")
print(f"Passed: {value >= PASSING_SCORE}")
