# This example demonstrates scope and lifetime basics concepts.

PASSING_SCORE = 60


def classify(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= PASSING_SCORE:
        return "D"
    return "F"


value = int(input("Enter score: "))
grade = classify(value)

print(f"Grade: {grade}")
print(f"Passed: {value >= PASSING_SCORE}")
