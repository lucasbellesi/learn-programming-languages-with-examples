# This example shows cleaning and combining text while preserving readable string logic.
# In Python, the example favors direct readable steps while keeping validation visible.

# Run one direct scenario at the top level so the printed result is easy to verify.
line = input("Enter a sentence: ")

cleaned_chars = []
for char in line:
    if char.isalnum():
        cleaned_chars.append(char.lower())
    else:
        cleaned_chars.append(" ")

cleaned = "".join(cleaned_chars)
words = [word for word in cleaned.split() if word]

# Print the observed state here so learners can match the code path to the result.
print(f"Normalized text: {cleaned}")
print(f"Tokens ({len(words)}):")
for word in words:
    print(f"- {word}")
