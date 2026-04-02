# Module focus: How names stay visible only inside the blocks that own them.
# Why it matters: practicing scope and lifetime basics patterns makes exercises and checkpoints
# easier to reason about.

# Walk through one fixed scenario so scope and lifetime basics behavior stays repeatable.
PASSING_SCORE = 60


# Helper setup for scope and lifetime basics; this keeps the walkthrough readable.
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

# Report values so learners can verify the scope and lifetime basics outcome.
print(f"Grade: {grade}")
print(f"Passed: {value >= PASSING_SCORE}")
