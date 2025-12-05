def solve(data: list[str]) -> int:
    dial_size = 100
    position = 50
    zero_count = 0

    for move in data:
        move = move.strip()
        if not move or len(move) < 2:
            raise ValueError(f"Invalid move instruction: {move}")

        direction = move[0]
        try:
            steps = int(move[1:])
        except ValueError:
            raise ValueError(f"Invalid step value in move: {move}")

        full_rotations, steps = divmod(steps, dial_size)
        zero_count += full_rotations
        # if full_rotations > 0:
        #    print(f"move: {move}, full_rotations {full_rotations}")

        if position == 0 and steps == 0:
            continue

        old_position = position
        if direction == "L":
            new_position = (position - steps) % dial_size
            # print(
            #    f"move: {move}, old_position: {old_position} and new_position: {new_position}"
            # )
            # left-shifting from 0 will always result in new_position greater than or equal to 0
            if old_position < new_position and old_position != 0:
                # Crossed zero
                zero_count += 1
                # print("crossed zero")
            position = new_position
        elif direction == "R":
            new_position = (position + steps) % dial_size
            # print(
            #    f"move: {move}, old_position: {old_position} and new_position: {new_position}"
            # )
            # right-shifting when ends at 0, will cause double count of zero position
            if old_position > new_position and new_position != 0:
                # Crossed zero
                zero_count += 1
                # print("crossed zero")
            position = new_position
        else:
            raise ValueError(f"Unexpected direction value: {direction}")

        if position == 0:
            zero_count += 1
            # print("current position is zero")

    return zero_count
