# This example shows counting repeated values and summarizing them through keyed lookups.
# In Python, the example favors direct readable steps while keeping validation visible.

# Run one deterministic scenario so the console output makes counting repeated values and
# summarizing them through keyed lookups easy to verify.
def main():
    # Build the sample state first, then let the later output confirm the behavior step by step.
    text = "banana bandana"
    frequencies = {}

    for ch in text:
        if ch == " ":
            continue

        frequencies[ch] = frequencies.get(ch, 0) + 1

    print("Character frequencies:")
    for key in sorted(frequencies):
        print(f"{key} -> {frequencies[key]}")


if __name__ == "__main__":
    main()
