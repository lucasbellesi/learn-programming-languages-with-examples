# Module focus: Cleaning and combining text while preserving readable string logic.
# Why it matters: practicing strings patterns makes exercises and checkpoints easier to reason
# about.

# Walk through one fixed scenario so strings behavior stays repeatable.
line = input("Enter a sentence: ")

cleaned_chars = []
for char in line:
    if char.isalnum():
        cleaned_chars.append(char.lower())
    else:
        cleaned_chars.append(" ")

cleaned = "".join(cleaned_chars)
words = [word for word in cleaned.split() if word]

# Report values so learners can verify the strings outcome.
print(f"Normalized text: {cleaned}")
print(f"Tokens ({len(words)}):")
for word in words:
    print(f"- {word}")
