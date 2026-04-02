# This helper example focuses on the repeated menu interaction without distracting setup code.

# This extra example extends control-flow with a menu-driven loop.

current_sum = 0

while True:
    print("\nMenu")
    print("1) Add number to sum")
    print("2) Show current sum")
    print("3) Reset sum")
    print("4) Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        raw_number = input("Enter a number: ").strip()
        try:
            number = int(raw_number)
        except ValueError:
            print("Invalid number. Try again.")
            continue

        current_sum += number
        print(f"Added. New sum is {current_sum}.")
    elif choice == "2":
        print(f"Current sum: {current_sum}")
    elif choice == "3":
        current_sum = 0
        print("Sum reset to 0.")
    elif choice == "4":
        print("Goodbye.")
        break
    else:
        print("Invalid option. Try again.")
