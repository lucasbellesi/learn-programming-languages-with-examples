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


def read_name(index: int) -> str:
    while True:
        name = input(f"Student #{index} name: ").strip()
        if name:
            return name

        print("Name cannot be empty.")


def read_score(name: str) -> int:
    while True:
        raw = input(f"{name}'s score (0-100): ").strip()
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
    total_students = read_positive_int("How many students? ")

    for index in range(1, total_students + 1):
        name = read_name(index)
        score = read_score(name)
        students.append({"name": name, "score": score})

    scores = [student["score"] for student in students]
    average = sum(scores) / len(scores)

    print("Students:")
    for student in students:
        print(f"- {student['name']}: {student['score']}")

    print(f"Average: {average:.2f}")
    print(f"Minimum: {min(scores)}")
    print(f"Maximum: {max(scores)}")


if __name__ == "__main__":
    main()
