raw_count = input("How many strings? ").strip()
if not raw_count.isdigit() or int(raw_count) <= 0:
    print("Please enter a positive count.")
else:
    count = int(raw_count)
    values: list[str] = []

    for index in range(count):
        text = input(f"String {index + 1}: ").strip()
        values.append(text)

        alias = values
        snapshot = values.copy()

        print(f"Current size: {len(values)}")
        print(f"Alias sees size: {len(alias)}")
        print(f"Snapshot size: {len(snapshot)}")
