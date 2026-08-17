# Module focus: How names stay visible only inside the blocks that own them.
# Why it matters: the example makes it possible to predict name visibility across nested
# scopes before the learner tackles the exercises.

# Fixed inputs make the consequence of using values before they are assigned in all branches
# visible and repeatable.
PASSING_SCORE = 60


# Separate helpers keep the main path focused on how to predict name visibility across nested
# scopes.
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

# The printed result shows whether the program can explain when values and resources cease to be
# usable.
print(f"Grade: {grade}")
print(f"Passed: {value >= PASSING_SCORE}")
