def solve(data: list[str]) -> int:
    dail = [i for i in range(100)]
    current_pos = 50
    count_zeros = 0

    for turn in data:
        turn = turn.strip()
        position = turn[0]
        move_by = int(turn[1:])
        # print(f"Old Current position: {current_pos}, turn: {turn}")
        if move_by >= len(dail):
            complete_rotations = move_by // len(dail)
            move_by = move_by % len(dail)
            count_zeros += complete_rotations
            # print("pointed to zero due to complete rotations")
            if move_by == 0 and current_pos == 0:
                continue
        match position:
            case "L":
                if current_pos != 0 and current_pos - move_by < 0:
                    # print("pointed to zero due to going less than zero")
                    count_zeros += 1
                current_pos = dail[current_pos - move_by]
            case "R":
                current_pos = current_pos + move_by
                if current_pos >= len(dail):
                    current_pos = dail[current_pos - len(dail)]
                    if current_pos != 0:
                        count_zeros += 1
                        # print("pointed to zero due to going more than 99")
            case _:
                raise ValueError(f"unexpected position value: {position}")
        if current_pos == 0:
            count_zeros += 1
        # print(f"New Current position: {current_pos}, count_zeros: {count_zeros}")

    return count_zeros
