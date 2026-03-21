score = int(input("Enter score (0-100): "))

if score < 0 or score > 100:
    print("Score must be between 0 and 100.")
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Grade: {grade}")
