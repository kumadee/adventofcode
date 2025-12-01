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

        if position == 0 and steps == 0:
            continue

        old_position = position
        if direction == "L":
            new_position = (position - steps) % dial_size
            if old_position > new_position:
                # Crossed zero
                zero_count += 1
            position = new_position
        elif direction == "R":
            new_position = (position + steps) % dial_size
            if new_position < old_position:
                # Crossed zero
                zero_count += 1
            position = new_position
        else:
            raise ValueError(f"Unexpected direction value: {direction}")

        if position == 0:
            zero_count += 1

    return zero_count
