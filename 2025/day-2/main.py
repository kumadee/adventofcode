import part1
import part2


def main():
    input_data = ""
    with open("input.txt") as f:
        input_data = f.read().split(",")
    answer = part1.solve(input_data)
    print(f"Part 1 answer: {answer}")
    answer = part2.solve(input_data)
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    main()
