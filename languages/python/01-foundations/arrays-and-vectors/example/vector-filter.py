# This helper example focuses on isolating one collection transformation so the filtering rule
# stands out.

# This extra example extends arrays-and-vectors with a focused filtering task.

raw_count = input("How many numbers? ").strip()
try:
    count = int(raw_count)
except ValueError:
    print("Please enter a positive count.")
else:
    if count <= 0:
        print("Please enter a positive count.")
    else:
        values = []
        for index in range(count):
            raw_value = input(f"Value {index + 1}: ").strip()
            try:
                values.append(int(raw_value))
            except ValueError:
                print("Please enter valid integers only.")
                break
        else:
            raw_threshold = input("Filter values greater than or equal to: ").strip()
            try:
                threshold = int(raw_threshold)
            except ValueError:
                print("Please enter a valid threshold.")
            else:
                filtered = [value for value in values if value >= threshold]
                if filtered:
                    print("Filtered values: " + ", ".join(str(value) for value in filtered))
                else:
                    print("Filtered values: none")
