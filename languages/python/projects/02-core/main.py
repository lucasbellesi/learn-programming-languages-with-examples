from pathlib import Path


def parse_record(line: str):
    parts = line.strip().split()
    if len(parts) < 2:
        return None

    try:
        score = int(parts[-1])
    except ValueError:
        return None

    if not 0 <= score <= 100:
        return None

    name = " ".join(parts[:-1]).strip()
    if not name:
        return None

    return {"name": name, "score": score}


def main() -> None:
    source_path = Path(input("Enter the input file path: ").strip())

    if not source_path.is_file():
        print("Input file not found.")
        return

    valid_records = []
    invalid_rows = 0

    for line in source_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue

        record = parse_record(line)
        if record is None:
            invalid_rows += 1
            continue

        valid_records.append(record)

    report_path = Path("report.txt")
    lines = [
        "Grade Report",
        f"Source file: {source_path}",
        f"Valid records: {len(valid_records)}",
        f"Invalid rows skipped: {invalid_rows}",
    ]

    if valid_records:
        average = sum(record["score"] for record in valid_records) / len(valid_records)
        lines.append(f"Average: {average:.2f}")
        lines.append("Students:")
        for record in valid_records:
            lines.append(f"- {record['name']}: {record['score']}")
        print(f"Valid records: {len(valid_records)}")
        print(f"Invalid rows skipped: {invalid_rows}")
        print(f"Average: {average:.2f}")
    else:
        lines.append("Average: N/A")
        lines.append("Students: none")
        print("Valid records: 0")
        print(f"Invalid rows skipped: {invalid_rows}")
        print("Average: N/A")

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Report written to report.txt")


if __name__ == "__main__":
    main()
