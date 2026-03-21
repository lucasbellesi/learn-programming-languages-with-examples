input_path = input("Input file path: ").strip()
output_path = input("Output file path: ").strip()

if not input_path or not output_path:
    print("Both paths are required.")
else:
    try:
        with open(input_path, "r", encoding="utf-8") as source, open(
            output_path, "w", encoding="utf-8"
        ) as destination:
            line_count = 0
            for line_count, line in enumerate(source, start=1):
                destination.write(f"{line_count}: {line}")

        print(f"Copied {line_count} lines.")
    except OSError:
        print("File processing failed.")
