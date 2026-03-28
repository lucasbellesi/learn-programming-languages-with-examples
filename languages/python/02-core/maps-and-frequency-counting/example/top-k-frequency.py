# This extra example extends maps-and-frequency-counting with ranked frequency output.
# Example purpose: count repeated words, then sort by frequency and name.

raw_count = input("How many words? ").strip()
try:
    count = int(raw_count)
except ValueError:
    print("Please enter a positive number.")
else:
    if count <= 0:
        print("Please enter a positive number.")
    else:
        frequency = {}
        for index in range(count):
            word = input(f"Word {index + 1}: ").strip()
            frequency[word] = frequency.get(word, 0) + 1

        raw_k = input("How many top words to show? ").strip()
        try:
            k = int(raw_k)
        except ValueError:
            print("Please enter a positive value for k.")
        else:
            if k <= 0:
                print("Please enter a positive value for k.")
            else:
                items = sorted(frequency.items(), key=lambda entry: (-entry[1], entry[0]))
                limited = items[:k]

                print(f"\nTop {len(limited)} words:")
                for index, (word, word_count) in enumerate(limited, start=1):
                    print(f"{index}. {word} -> {word_count}")
