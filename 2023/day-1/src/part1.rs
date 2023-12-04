fn line_to_number(line: &str) -> u32 {
    let mut first_digit: u32 = 0;
    let mut second_digit: u32 = 0;
    for c in line.chars() {
        if c.is_digit(10) {
            if first_digit == 0 && second_digit == 0 {
                first_digit = c.to_digit(10).unwrap();
                second_digit = first_digit;
            } else {
                second_digit = c.to_digit(10).unwrap();
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
        assert_eq!(12, line_to_number("1abc2"));
        assert_eq!(15, line_to_number("a1b2c3d4e5f"));
        assert_eq!(77, line_to_number("treb7uchet"));
    }

    #[test]
    fn test_multi_lines() {
        let input = "1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet";
        assert_eq!(142, solve(input));
    }
}
