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

        steps %= dial_size  # Ensure steps are within dial bounds

        if direction == "L":
            position = (position - steps) % dial_size
        elif direction == "R":
            position = (position + steps) % dial_size
        else:
            raise ValueError(f"Unexpected direction value: {direction}")

        if position == 0:
            zero_count += 1

    return zero_count
