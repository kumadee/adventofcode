def find_joltage(bank: str, battery_size: int) -> int:
    batteries = ""

    frequency = {}
    for d in bank:
        if d not in frequency:
            frequency[d] = 1
        else:
            frequency[d] += 1

    ordered_digits = sorted(frequency.keys(), reverse=True)

    curr_index = 0
    for _ in range(battery_size):
        curr_battery_size = len(batteries)
        digits_index = {i: bank.find(i, curr_index) for i in ordered_digits}
        places_to_fill_in_battery = battery_size - curr_battery_size
        for digit in ordered_digits:
            digit_index = digits_index[digit]
            if digit_index == -1:
                continue
            # check if the digit_index is at a position such that
            # the remaining digits after the digit_index in bank is
            # greater than or equal to remaining places to fill in batteries
            remaining_digits_from_digit_index = len(bank) - digit_index
            if places_to_fill_in_battery <= remaining_digits_from_digit_index:
                batteries += digit
                curr_index = digit_index + 1
                break
        for k, v in digits_index.items():
            if v == -1:
                ordered_digits.remove(k)

    joltage = int(batteries)
    # print(f"bank: {bank}, joltage: {joltage:_}")
    return joltage


def solve(data: list[str], battery_size: int = 12) -> int:
    return sum([find_joltage(bank.strip(), battery_size) for bank in data])
