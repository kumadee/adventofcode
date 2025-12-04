class Matrix:
    def __init__(self) -> None:
        self.grid: list[list[int]] = []
        self.total_row_count: int = 0
        self.total_column_count: int = 0
        pass

    def create_adjacency_matrix(self, grid: list[str]) -> None:
        for _line in grid:
            line = _line.strip()
            # skip empty lines
            if len(line) == 0:
                continue

            if self.total_column_count == 0:
                self.total_column_count = len(line)
            elif len(line) != self.total_column_count:
                raise ValueError(
                    f"Expected column count from 1st line: {self.total_column_count}, irregular column count for line {line}"
                )
            row = []
            for roll in line:
                if roll == ".":
                    row.append(0)
                elif roll == "@":
                    row.append(1)
                else:
                    raise ValueError(
                        f"Unexpected value of roll: {roll} in line: {line}"
                    )
            self.grid.append(row)
            self.total_row_count += 1

    def find_neighbours_count(self, column: int, row: int) -> int:
        neighbours_count = 0
        neighbour_coordinates = {
            "up": (column, row - 1),
            "down": (column, row + 1),
            "left": (column - 1, row),
            "right": (column + 1, row),
            "up-left": (column - 1, row - 1),
            "up-right": (column + 1, row - 1),
            "down-left": (column - 1, row + 1),
            "down-right": (column + 1, row + 1),
        }
        for position, coordinates in neighbour_coordinates.items():
            # print(f"Checking for position {position} and coordinates: {coordinates}")
            # ignore the coordinates that are not out of bounds
            (n_column, n_row) = coordinates
            if n_row >= self.total_row_count or n_row < 0:
                continue
            if n_column >= self.total_column_count or n_column < 0:
                continue
            # if grid value is 1, then neighbour exists
            if self.grid[n_row][n_column] == 1:
                neighbours_count += 1

        return neighbours_count


def accessible_rolls_via_forklift(matrix: Matrix) -> int:
    accessible_rolls_count = 0
    limit = 4
    for row in range(matrix.total_row_count):
        for col in range(matrix.total_column_count):
            if matrix.grid[row][col] == 0:
                # print(
                #    f"For (row, col) = ({row}, {col}), neighbours count: 0 due to nothing"
                # )
                continue
            count = matrix.find_neighbours_count(col, row)
            # print(f"For (row, col) = ({row}, {col}), neighbours count: {count}")
            if count < limit:
                # print(f"Accessible (row, col) = ({row}, {col})")
                accessible_rolls_count += 1

    return accessible_rolls_count


def solve(data: list[str]) -> int:
    matrix = Matrix()
    matrix.create_adjacency_matrix(data)
    # print(matrix.grid)
    print(
        f"size total rows: {matrix.total_row_count}, total columns: {matrix.total_column_count}"
    )
    return accessible_rolls_via_forklift(matrix)
