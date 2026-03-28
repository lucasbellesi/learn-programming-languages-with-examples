# This extra example extends functions with runtime-type dispatch.
# Example purpose: mirror overload-style behavior in a language without signature overloading.


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
