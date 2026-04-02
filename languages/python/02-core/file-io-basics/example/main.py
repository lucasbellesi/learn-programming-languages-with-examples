# Module focus: Reading plain-text files, parsing rows, and writing clear results.
# Why it matters: practicing file io basics patterns makes exercises and checkpoints easier to
# reason about.

from pathlib import Path
import tempfile


# Helper setup for file io basics; this keeps the walkthrough readable.
def parse_score_row(line):
    # Prepare sample inputs that exercise the key file io basics path.
    parts = line.strip().split()
    if len(parts) != 2:
        return None

    try:
        score = int(parts[1])
    except ValueError:
        return None

    return parts[0], score


# Walk through one fixed scenario so file io basics behavior stays repeatable.
def main():
    base_dir = Path(tempfile.gettempdir()) / "learn-lang-file-io-python"
    base_dir.mkdir(parents=True, exist_ok=True)
    input_path = base_dir / "scores.txt"
    output_path = base_dir / "summary.txt"

    if not input_path.exists():
        input_path.write_text("ana 90\nbob 82\ninvalid row\ncarla 95\n", encoding="utf-8")

    valid_rows = 0
    score_sum = 0

    with input_path.open("r", encoding="utf-8") as source:
        for raw_line in source:
            parsed = parse_score_row(raw_line)
            if parsed is None:
                continue

            name, score = parsed
            valid_rows += 1
            score_sum += score
            # Report output values so learners can verify the file io basics outcome.
            print(f"{name} -> {score}")

    if valid_rows == 0:
        print("No valid rows found.")
        return

    average = score_sum / valid_rows
    output_path.write_text(f"Rows: {valid_rows}\nAverage: {average:.2f}\n", encoding="utf-8")
    print(f"Summary written to {output_path}")


if __name__ == "__main__":
    main()
