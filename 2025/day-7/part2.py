START_POINT = "S"
EMPTY_SPACE = "."
BEAM = "|"
SPLITTER = "^"


def count_timelines(diagram: list[str]) -> int:
    rows = len(diagram)
    cols = len(diagram[0]) if rows > 0 else 0

    # Memoization cache: (row, col) -> number of timelines
    memo: dict[tuple[int, int], int] = {}

    def backtrack(row: int, col: int) -> int:
        # Base case: out of bounds
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return 1  # One timeline exits the manifold

        # Check memoization cache
        if (row, col) in memo:
            return memo[(row, col)]

        cell = diagram[row][col]

        # If it's empty space or starting point, continue downward
        if cell == EMPTY_SPACE or cell == START_POINT:
            result = backtrack(row + 1, col)

        # If it's a splitter, split into two paths (left and right)
        elif cell == SPLITTER:
            left_timelines = backtrack(row + 1, col - 1)
            right_timelines = backtrack(row + 1, col + 1)
            result = left_timelines + right_timelines

        else:
            result = 0

        memo[(row, col)] = result
        return result

    # Start backtracking from the starting position
    return backtrack(0, diagram[0].index(START_POINT))


def solve(data: list[str]) -> int:
    return count_timelines(data)
