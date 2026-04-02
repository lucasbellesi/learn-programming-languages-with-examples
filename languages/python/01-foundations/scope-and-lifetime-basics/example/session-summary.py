# This helper example focuses on isolating one scope-sensitive helper so lifetime differences stay
# visible.

# This extra example extends scope and lifetime basics with a session summary.

BONUS_POINTS = 5
PASSING_SCORE = 70


# Keep this helper separate so the main example can focus on the larger idea without extra noise.
def summarize_attempt(name, score):
    effective_score = score + BONUS_POINTS
    passed = effective_score >= PASSING_SCORE
    status = "passed" if passed else "needs review"
    return f"{name}: raw={score}, effective={effective_score}, status={status}", passed


attempts = [("Ana", 64), ("Bruno", 71), ("Carla", 58)]
passed_count = 0

for student_name, raw_score in attempts:
    line, passed = summarize_attempt(student_name, raw_score)
    print(line)
    if passed:
        passed_count += 1

print(f"Students above the target: {passed_count}")
