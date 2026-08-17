def run_smart_pointers_in_depth_exercise() -> None:
    source_title = input()
    destination_title = input()
    # TODO 1: Convert `empty` to a null holder and other lines to owned notes.
    # TODO 2: Move an owned note between holders.
    # TODO 3: Produce ownership transfer logs before and after moving; verify moving from an empty
    #         holder; destination already occupied.
    _ = source_title, destination_title


def main() -> None:
    run_smart_pointers_in_depth_exercise()


if __name__ == "__main__":
    main()
