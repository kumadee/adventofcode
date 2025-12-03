def find_joltage(bank: int) -> int:
    original_bank = bank
    (bank, least_significant_digit) = divmod(bank, 10)
    (bank, most_significant_digit) = divmod(bank, 10)
    while bank != 0:
        (bank, _digit) = divmod(bank, 10)
        if most_significant_digit == 0:
            most_significant_digit = _digit
            continue
        if _digit >= most_significant_digit:
            if least_significant_digit < most_significant_digit:
                least_significant_digit = most_significant_digit
            most_significant_digit = _digit

    if most_significant_digit == 0 or least_significant_digit == 0:
        raise ValueError(
            f"For bank: {original_bank}, the most_significant_digit: {most_significant_digit} or the least_significant_digit: {least_significant_digit} is invalid"
        )
    joltage = most_significant_digit * 10 + least_significant_digit
    # print(f"bank: {original_bank}, joltage: {joltage}")
    return joltage


def solve(data: list[str]) -> int:
    return sum([find_joltage(int(bank)) for bank in data])
