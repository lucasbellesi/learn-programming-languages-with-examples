total_seconds = int(input("Enter total seconds: "))

if total_seconds < 0:
    print("Please enter a non-negative value.")
else:
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    print(f"Hours: {hours}")
    print(f"Minutes: {minutes}")
    print(f"Seconds: {seconds}")
