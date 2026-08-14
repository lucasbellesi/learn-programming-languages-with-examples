def parse_score_row(line):
    parts = line.strip().split()
    if len(parts) != 2:
        return None

    try:
        return int(parts[1])
    except ValueError:
        return None


path = input("Enter file path (name score rows): ").strip()

try:
    with open(path, "r", encoding="utf-8") as source:
        valid_rows = 0
        invalid_rows = 0
        score_sum = 0

        for line in source:
            score = parse_score_row(line)
            if score is None:
                invalid_rows += 1
            else:
                valid_rows += 1
                score_sum += score

    print(f"Valid rows: {valid_rows}")
    print(f"Invalid rows: {invalid_rows}")

    if valid_rows > 0:
        average = score_sum / valid_rows
        print(f"Average score: {average:.2f}")
    else:
        print("No valid rows found.")
except OSError:
    print("Could not open file.")
