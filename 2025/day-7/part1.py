START_POINT = "S"
EMPTY_SPACE = "."
BEAM = "|"
SPLITTER = "^"


def create_matrix(data: list[str]) -> list[list[str]]:
    matrix = []
    for row in data:
        matrix.append(list(row))
    return matrix


def print_matrix(matrix) -> None:
    for row in matrix:
        print("".join(row))


def solve(data: list[str]) -> int:
    split_count = 0
    matrix: list[list[str]] = create_matrix(data)
    for i, row in enumerate(matrix):
        for j in range(len(row)):
            point = row[j]
            if point == START_POINT:
                break
            if point == EMPTY_SPACE and (
                matrix[i - 1][j] == START_POINT or matrix[i - 1][j] == BEAM
            ):
                matrix[i][j] = BEAM
            if point == SPLITTER and matrix[i - 1][j] == BEAM:
                if row[j - 1] == BEAM and row[j + 1] == BEAM:
                    continue
                if row[j - 1] == EMPTY_SPACE or row[j + 1] == EMPTY_SPACE:
                    split_count += 1
                if row[j - 1] == EMPTY_SPACE:
                    row[j - 1] = BEAM
                if row[j + 1] == EMPTY_SPACE:
                    row[j + 1] = BEAM
    # print_matrix(matrix)
    return split_count
