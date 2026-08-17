# Module focus: Cleaning and combining text while preserving readable string logic.
# Why it matters: the example makes it possible to normalize, inspect, and transform textual data
# before the learner tackles the exercises.
# about.

# Fixed inputs make the consequence of counting words without removing extra spaces visible and
# repeatable.
line = input("Enter a sentence: ")

cleaned_chars = []
for char in line:
    if char.isalnum():
        cleaned_chars.append(char.lower())
    else:
        cleaned_chars.append(" ")

cleaned = "".join(cleaned_chars)
words = [word for word in cleaned.split() if word]

# The printed result shows whether the program can handle empty input and character boundaries
# safely.
print(f"Normalized text: {cleaned}")
print(f"Tokens ({len(words)}):")
for word in words:
    print(f"- {word}")
