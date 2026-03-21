# This example demonstrates strings concepts.
# Example purpose: show the module flow with clear, beginner-friendly steps.

# Intent: gather typed input first so later operations are predictable.
line = input("Enter a sentence: ")

cleaned_chars = []
# Intent: iterate through data in a clear and deterministic order.
for char in line:
    # Intent: guard invalid or edge-case paths before the main path continues.
    if char.isalnum():
        cleaned_chars.append(char.lower())
    else:
        cleaned_chars.append(" ")

cleaned = "".join(cleaned_chars)
words = [word for word in cleaned.split() if word]

# Intent: print intermediate or final output for quick behavior verification.
print(f"Normalized text: {cleaned}")
print(f"Tokens ({len(words)}):")
for word in words:
    print(f"- {word}")
