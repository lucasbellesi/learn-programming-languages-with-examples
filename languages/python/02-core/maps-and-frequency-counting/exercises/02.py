text = input("Enter text: ")

frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

result = None
for ch in text:
    if frequency[ch] == 1:
        result = ch
        break

if result is None:
    print("No non-repeating character found.")
else:
    print(f"First non-repeating character: {result}")
