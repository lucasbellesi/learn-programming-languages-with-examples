def max_of_three(a, b, c):
    return max(a, b, c)


x, y, z = map(int, input("Enter three integers: ").split())
print(f"Maximum: {max_of_three(x, y, z)}")
