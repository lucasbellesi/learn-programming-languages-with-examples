text = input("Enter text: ")
normalized = "".join(char.lower() for char in text if char.isalpha())

if not normalized:
    print("No letters to evaluate.")
elif normalized == normalized[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
