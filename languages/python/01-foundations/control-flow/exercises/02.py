print("Enter integers (-1 to stop):")
values = []

while True:
    current = int(input())
    if current == -1:
        break
    values.append(current)

if not values:
    print("No values entered.")
else:
    print(f"Average: {sum(values) / len(values)}")
