from part_01 import load_puzzle_input


def main() -> None:
    left, right = load_puzzle_input(puzzle="input.txt")

    left_item_frequency_in_right = {}

    for item in right:
        if item not in left_item_frequency_in_right:
            left_item_frequency_in_right[item] = 1
        else:
            left_item_frequency_in_right[item] += 1

    distance = 0

    for item in left:
        if item in left_item_frequency_in_right:
            distance += int(item) * int(left_item_frequency_in_right[item])

    print(f"Total distance: {distance}")


if __name__ == "__main__":
    main()
