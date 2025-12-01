def solve(data: list[str]) -> int:
    dail = [i for i in range(100)]
    current_pos = 50
    count_zeros = 0

    for turn in data:
        turn = turn.strip()
        position = turn[0]
        move_by = int(turn[1:])
        if move_by >= len(dail):
            move_by = move_by % len(dail)
        # print(f"Old Current position: {current_pos}, turn: {turn}")
        match position:
            case "L":
                current_pos = dail[current_pos - move_by]
            case "R":
                current_pos = current_pos + move_by
                if current_pos >= len(dail):
                    current_pos = dail[current_pos - len(dail)]
            case _:
                raise ValueError(f"unexpected position value: {position}")
        # print(f"New Current position: {current_pos}")
        if current_pos == 0:
            count_zeros += 1

    return count_zeros
