use std::collections::HashMap;

fn line_to_number(line: &str, nums: &HashMap<String, u32>) -> u32 {
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
            println!("{}", spelled_digit);
            for (i, key) in nums.keys().enumerate() {
                if spelled_digit.len() <= key.len() && key.starts_with(&spelled_digit) {
                    break;
                }
                if i == 8 {
                    spelled_digit = String::from(c);
                }
            }
            println!("{:?}", nums.get(&spelled_digit));
            if let Some(digit) = nums.get(&spelled_digit) {
                if first_digit == 0 && second_digit == 0 {
                    first_digit = *digit;
                    second_digit = first_digit;
                } else {
                    second_digit = *digit;
                }

                spelled_digit = match c {
                    'e' | 'o' | 'n' | 't' => String::from(c),
                    _ => String::from(""),
                };
            }
        }
    }
    let res = first_digit * 10 + second_digit;
    //println!("{} = {}", line, res);
    res
}

fn get_nums() -> HashMap<String, u32> {
    [
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
    .into()
}

pub fn solve(text: &str) -> u32 {
    text.lines()
        .map(|line| line_to_number(line.trim_start(), &get_nums()))
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_single_line() {
        let nums: HashMap<String, u32> = get_nums();
        // assert_eq!(29, line_to_number("two1nine", &nums));
        // assert_eq!(13, line_to_number("abcone2threexyz", &nums));
        // assert_eq!(76, line_to_number("7pqrstsixteen", &nums));
        // assert_eq!(51, line_to_number("fivezg8jmf6hrxnhgxxttwoneg", &nums));
        // assert_eq!(81, line_to_number("hgneightwogrfkcxpthree98threefourxshxvpbone", &nums));
        assert_eq!(39, line_to_number("plptcvbzh3fourfiveczxdrckjbg8twoninecrhfkll", &nums))
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
        assert_eq!(281, solve(input));
    }
}
