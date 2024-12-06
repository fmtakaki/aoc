def main() -> None:
    with open(file="input.txt", mode="r", encoding="utf-8") as file:
        puzzle = file.readlines()

        safe_reports = 0
        for line in puzzle:
            l = line.replace("\n", "").split(" ")

            level_evaluator = lambda x: x == 0 or x > 3
            level_dif = [
                level_evaluator(abs(int(j) - int(i))) for i, j in zip(l, l[1:])
            ]

            if True not in level_dif:
                level_direction = lambda x: -1 if x < 0 else 1
                level_dif = sum(
                    [level_direction(int(i) - int(j)) for i, j in zip(l, l[1:])]
                )

                if level_dif == (len(l) - 1) * -1 or level_dif == (len(l) - 1):
                    safe_reports += 1

        print(f"Total safe reports: {safe_reports}")  # Right answer: 534


if __name__ == "__main__":
    main()
