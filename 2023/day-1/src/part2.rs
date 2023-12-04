use std::collections::HashMap;

fn line_to_number(line: &str) -> u32 {
    let nums: HashMap<String, u32> = [
        (String::from("one"), 1),
        (String::from("two"), 2),
        (String::from("three"), 3),
        (String::from("four"), 4),
        (String::from("five"), 5),
        (String::from("six"), 6),
        (String::from("seven"), 7),
        (String::from("eight"), 8),
        (String::from("nine"), 9),
    ]
    .into();

    let mut first_digit: u32 = 0;
    let mut second_digit: u32 = 0;
    let mut spelled_digit: String = String::from("");
    for c in line.chars() {
        if c.is_digit(10) {
            spelled_digit = String::from("");
            if first_digit == 0 && second_digit == 0 {
                first_digit = c.to_digit(10).unwrap();
                second_digit = first_digit;
            } else {
                second_digit = c.to_digit(10).unwrap();
            }
        } else {
            spelled_digit.push(c);
            if let Some(digit) = nums.get(&spelled_digit) {
                if first_digit == 0 && second_digit == 0 {
                    first_digit = *digit;
                    second_digit = first_digit;
                } else {
                    second_digit = *digit;
                }
                spelled_digit = String::from("");
            }
        }
    }
    first_digit * 10 + second_digit
}

pub fn solve(text: &str) -> u32 {
    text.lines().map(|line| line_to_number(line)).sum()
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_single_line() {
        assert_eq!(29, line_to_number("two1nine"));
        assert_eq!(13, line_to_number("abcone2threexyz"));
        assert_eq!(76, line_to_number("7pqrstsixteen"));
    }

    #[test]
    fn test_multi_lines() {
        let input = "two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen";
        assert_eq!(142, solve(input));
    }
}
