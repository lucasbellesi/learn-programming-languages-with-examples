# This helper example focuses on showing one focused overload or helper so the main example stays
# easy to scan.

# This extra example extends functions with runtime-type dispatch.

# Keep this helper separate so the main example can focus on the larger idea without extra noise.
def print_value(value):
    if isinstance(value, bool):
        print(f"Boolean value: {value}")
    elif isinstance(value, int):
        print(f"Integer value: {value}")
    elif isinstance(value, float):
        print(f"Float value: {value}")
    elif isinstance(value, str):
        print(f"String value: {value}")
    else:
        print(f"Unsupported value: {value!r}")


print_value(42)
print_value(3.14159)
print_value("Hello from runtime dispatch")
