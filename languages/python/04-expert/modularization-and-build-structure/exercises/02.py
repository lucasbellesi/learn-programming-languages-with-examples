def build_registry():
    return {
        "add": lambda left, right: (left + right, True),
        "sub": lambda left, right: (left - right, True),
        "mul": lambda left, right: (left * right, True),
        "div": lambda left, right: (0, False) if right == 0 else (left // right, True),
    }


def main() -> None:
    command = input("Command: ").strip()
    try:
        left = int(input("Left operand: "))
        right = int(input("Right operand: "))
    except ValueError:
        print("Invalid input.")
        return

    registry = build_registry()
    handler = registry.get(command)
    if handler is None:
        print("Unsupported command.")
        return

    result, success = handler(left, right)
    if not success:
        print("Operation failed.")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
