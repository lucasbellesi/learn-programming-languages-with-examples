def read_positive_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if value <= 0:
            print("Please enter a number greater than zero.")
            continue

        return value


def read_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value

        print("This value cannot be empty.")


def read_score(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            score = int(raw)
        except ValueError:
            print("Please enter a valid integer score.")
            continue

        if 0 <= score <= 100:
            return score

        print("Score must be between 0 and 100.")


def main() -> None:
    students = []
    count = read_positive_int("How many students? ")

    for index in range(1, count + 1):
        name = read_non_empty(f"Student #{index} name: ")
        score = read_score(f"{name}'s score (0-100): ")
        students.append({"name": name, "score": score})

    total = sum(student["score"] for student in students)
    average = total / len(students)
    highest = max(students, key=lambda student: student["score"])
    lowest = min(students, key=lambda student: student["score"])
    passed = sum(1 for student in students if student["score"] >= 60)

    print("Students:")
    for student in students:
        print(f"- {student['name']}: {student['score']}")

    print(f"Average: {average:.2f}")
    print(f"Highest: {highest['name']} ({highest['score']})")
    print(f"Lowest: {lowest['name']} ({lowest['score']})")
    print(f"Passed: {passed}/{len(students)}")


if __name__ == "__main__":
    main()
