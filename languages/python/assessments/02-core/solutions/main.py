from pathlib import Path


def build_frequency(scores: list[int]) -> list[tuple[str, int]]:
    buckets = []
    for start in range(0, 100, 10):
        end = 100 if start == 90 else start + 9
        label = f"{start}-{end}"
        count = sum(1 for score in scores if start <= score <= end)
        buckets.append((label, count))
    return buckets


def main() -> None:
    scores = []

    while True:
        raw = input("Enter a score (0-100) or -1 to finish: ").strip()
        try:
            value = int(raw)
        except ValueError:
            print("Invalid integer. Try again.")
            continue

        if value == -1:
            break

        if not 0 <= value <= 100:
            print("Score ignored because it is outside 0-100.")
            continue

        scores.append(value)

    frequency = build_frequency(scores)
    lines = [f"Valid scores: {len(scores)}"]

    if scores:
        average = sum(scores) / len(scores)
        lines.append(f"Average: {average:.2f}")
        lines.append(f"Minimum: {min(scores)}")
        lines.append(f"Maximum: {max(scores)}")
    else:
        lines.append("Average: N/A")
        lines.append("Minimum: N/A")
        lines.append("Maximum: N/A")

    lines.append("Frequency:")
    for label, count in frequency:
        lines.append(f"- {label}: {count}")

    for line in lines:
        print(line)

    report_path = Path("core_assessment_report.txt")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Report written to core_assessment_report.txt")


if __name__ == "__main__":
    main()
