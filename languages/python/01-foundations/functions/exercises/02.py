def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels)


line = input("Enter text: ")
print(f"Number of vowels: {count_vowels(line)}")
