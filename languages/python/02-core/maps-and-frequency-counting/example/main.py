# Module focus: Counting repeated values and summarizing them through keyed lookups.
# Why it matters: the example makes it possible to use key-value collections to aggregate and
# retrieve data before the learner tackles the exercises.

# Fixed inputs make the consequence of assuming missing keys already exist visible and repeatable.
def main():
    # These values exercise the normal path before the exercises vary the documented boundaries.
    text = "banana bandana"
    frequencies = {}

    for ch in text:
        if ch == " ":
            continue

        frequencies[ch] = frequencies.get(ch, 0) + 1

    # The printed result shows whether the program can define normalization and missing-key
    # behavior explicitly.
    print("Character frequencies:")
    for key in sorted(frequencies):
        print(f"{key} -> {frequencies[key]}")


if __name__ == "__main__":
    main()
