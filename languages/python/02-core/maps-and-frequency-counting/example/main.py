# Module focus: Counting repeated values and summarizing them through keyed lookups.
# Why it matters: practicing maps and frequency counting patterns makes exercises and checkpoints
# easier to reason about.

# Walk through one fixed scenario so maps and frequency counting behavior stays repeatable.
def main():
    # Prepare sample inputs that exercise the key maps and frequency counting path.
    text = "banana bandana"
    frequencies = {}

    for ch in text:
        if ch == " ":
            continue

        frequencies[ch] = frequencies.get(ch, 0) + 1

    # Report output values so learners can verify the maps and frequency counting outcome.
    print("Character frequencies:")
    for key in sorted(frequencies):
        print(f"{key} -> {frequencies[key]}")


if __name__ == "__main__":
    main()
