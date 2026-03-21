# Example purpose: show the module flow with clear, beginner-friendly steps.


def main():
    # Program flow: iterate text, count symbols, then print a frequency table.
    text = "banana bandana"
    frequencies = {}

    # Intent: process characters in source order before aggregation.
    for ch in text:
        # Intent: skip separators so counts represent meaningful symbols.
        if ch == " ":
            continue

        frequencies[ch] = frequencies.get(ch, 0) + 1

    # Intent: print final frequencies in sorted-key order for deterministic output.
    print("Character frequencies:")
    for key in sorted(frequencies):
        print(f"{key} -> {frequencies[key]}")


if __name__ == "__main__":
    main()
