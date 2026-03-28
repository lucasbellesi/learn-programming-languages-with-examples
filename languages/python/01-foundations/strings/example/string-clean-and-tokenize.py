# This extra example extends strings with text normalization and token extraction.
# Example purpose: separate character cleanup from token building.

line = input("Enter a sentence: ")

cleaned_chars = []
for char in line:
    if char.isalnum():
        cleaned_chars.append(char.lower())
    else:
        cleaned_chars.append(" ")

cleaned = "".join(cleaned_chars)

words = []
current_word = []
for char in cleaned:
    if char == " ":
        if current_word:
            words.append("".join(current_word))
            current_word = []
    else:
        current_word.append(char)

if current_word:
    words.append("".join(current_word))

print(f"Normalized text: {cleaned}")
print(f"Tokens ({len(words)}):")
for word in words:
    print(f"- {word}")
