# This example shows how names stay visible only inside the blocks that own them.
# In Python, the example favors direct readable steps while keeping validation visible.

# Run one direct scenario at the top level so the printed result is easy to verify.
PASSING_SCORE = 60


# Define the reusable pieces first so the later top-level flow stays easy to read.
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

# Print the observed state here so learners can match the code path to the result.
print(f"Grade: {grade}")
print(f"Passed: {value >= PASSING_SCORE}")
