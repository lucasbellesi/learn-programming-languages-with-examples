# This example demonstrates strings concepts.

line = input("Enter a sentence: ")

cleaned_chars = []
for char in line:
    if char.isalnum():
        cleaned_chars.append(char.lower())
    else:
        cleaned_chars.append(" ")

cleaned = "".join(cleaned_chars)
words = [word for word in cleaned.split() if word]

print(f"Normalized text: {cleaned}")
print(f"Tokens ({len(words)}):")
for word in words:
    print(f"- {word}")
