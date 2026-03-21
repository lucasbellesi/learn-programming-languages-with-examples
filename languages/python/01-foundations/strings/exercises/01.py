line = input("Enter text: ")
words = [word for word in line.strip().split() if word]

print(f"Word count: {len(words)}")
