# This example shows reading plain-text files, parsing rows, and writing clear results.
# In Python, the example favors direct readable steps while keeping validation visible.

from pathlib import Path
import tempfile


# Define the reusable pieces first so the main flow can focus on one observable scenario.
def parse_score_row(line):
    # Build the sample state first, then let the later output confirm the behavior step by step.
    parts = line.strip().split()
    if len(parts) != 2:
        return None

    try:
        score = int(parts[1])
    except ValueError:
        return None

    return parts[0], score


# Run one deterministic scenario so the console output makes reading plain-text files, parsing rows,
# and writing clear results easy to verify.
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
            print(f"{name} -> {score}")

    if valid_rows == 0:
        print("No valid rows found.")
        return

    average = score_sum / valid_rows
    output_path.write_text(f"Rows: {valid_rows}\nAverage: {average:.2f}\n", encoding="utf-8")
    print(f"Summary written to {output_path}")


if __name__ == "__main__":
    main()
