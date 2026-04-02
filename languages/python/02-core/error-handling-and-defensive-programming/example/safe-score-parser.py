# This helper example focuses on isolating the parsing guard so invalid text never silently becomes
# a score.

# This extra example extends defensive programming with safe score parsing.

# Keep this helper separate so the main example can focus on the larger idea without extra noise.
def try_parse_row(row):
    parts = row.split(":")
    if len(parts) != 2:
        return None

    name = parts[0].strip()
    if not name:
        return None

    try:
        score = int(parts[1].strip())
    except ValueError:
        return None

    if score < 0 or score > 100:
        return None

    return name, score


rows = ["Ana: 91", "InvalidRow", "Bruno: not-a-number", "Carla: 77", "Diego: 130"]
valid_rows = []

for row in rows:
    parsed = try_parse_row(row)
    if parsed is None:
        print(f"Skipping invalid row: {row}")
        continue

    valid_rows.append(parsed)

print(f"Valid rows: {len(valid_rows)}")
for name, score in valid_rows:
    print(f"- {name} => {score}")
