row = input("Enter row (name,age,city): ")

first_comma = row.find(",")
if first_comma < 0:
    print("Invalid format. Missing commas.")
else:
    second_comma = row.find(",", first_comma + 1)
    if second_comma < 0:
        print("Invalid format. Missing second comma.")
    else:
        name = row[:first_comma]
        age = row[first_comma + 1 : second_comma]
        city = row[second_comma + 1 :]

        if not name or not age or not city:
            print("Invalid format. Empty field detected.")
        else:
            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"City: {city}")
