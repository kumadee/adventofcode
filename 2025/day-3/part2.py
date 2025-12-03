def find_joltage(bank: int) -> int:
    original_bank = bank
    battery_size = 12
    (bank, battery) = divmod(bank, 10**battery_size)

    batteries = [0 for _ in range(battery_size)]  # least significant digits start first
    for i in range(battery_size):
        (battery, batteries[i]) = divmod(battery, 10)

    while bank != 0:
        (bank, last_digit) = divmod(bank, 10)

        for i in range(battery_size - 1, 0, -1):
            if last_digit < batteries[i]:
                break
            tmp = batteries[i]
            batteries[i] = last_digit
            last_digit = tmp

    for battery in batteries:
        if battery == 0:
            raise ValueError(
                f"For bank: {original_bank}, the batteries: {batteries} is invalid"
            )
    joltage = 0
    for i, battery in enumerate(batteries):
        joltage = battery * 10**i + joltage
    print(f"bank: {original_bank}, joltage: {joltage}")
    return joltage


def solve(data: list[str]) -> int:
    return sum([find_joltage(int(bank)) for bank in data])
