# This extra example extends algorithms basics with a best-streak scan.
# Example purpose: track the longest rising streak with one pass.


def longest_rising_streak(values):
    if not values:
        return 0, []

    best_length = 1
    best_start = 0
    current_length = 1
    current_start = 0

    for index in range(1, len(values)):
        if values[index] > values[index - 1]:
            current_length += 1
        else:
            current_length = 1
            current_start = index

        if current_length > best_length:
            best_length = current_length
            best_start = current_start

    best_values = values[best_start : best_start + best_length]
    return best_length, best_values


temperatures = [17, 18, 21, 19, 20, 22, 25, 24]
length, streak = longest_rising_streak(temperatures)

print(f"Longest rising streak length: {length}")
print(f"Streak values: {streak}")
