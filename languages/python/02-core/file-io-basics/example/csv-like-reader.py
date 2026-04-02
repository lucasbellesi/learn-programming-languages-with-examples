# This helper example focuses on separating row parsing from the higher-level file workflow.

# This extra example extends file-io-basics with line parsing and validation.

path = input("CSV-like input file path (name,score): ").strip()

try:
    with open(path, "r", encoding="utf-8") as handle:
        rows = []
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue

            if "," not in line:
                print(f"Skipping malformed line {line_number}: {line}")
                continue

            name, score_text = line.split(",", 1)
            try:
                score = int(score_text)
            except ValueError:
                print(f"Skipping invalid score on line {line_number}: {score_text}")
                continue

            if score < 0 or score > 100:
                print(f"Skipping invalid score on line {line_number}: {score_text}")
                continue

            rows.append((name, score))
except OSError:
    print(f"Could not open file: {path}")
else:
    print(f"\nValid rows: {len(rows)}")
    for name, score in rows:
        print(f"- {name}: {score}")
