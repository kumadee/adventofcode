use std::collections::HashSet;

pub fn solve(input: &str) -> u32 {
    let mut points: Vec<u32> = Vec::new();
    for line in input.lines() {
        let colon_idx = match line.find(":") {
            Some(c) => c,
            None => 0,
        };
        // println!("card num: {}, line: {}", card_num, &line[colon_idx..]);
        let pipe_idx = match line.find("|") {
            Some(c) => c,
            None => 0,
        };
        let scratchcard_nums: HashSet<u32> = line[colon_idx..pipe_idx]
            .trim()
            .split_whitespace()
            .map(|d| d.parse::<u32>().unwrap_or_default())
            .filter(|d| *d != 0)
            .collect();
        // println!("{:?}", scratchcard_nums);
        let nums_in_hand: HashSet<u32> = line[pipe_idx..]
            .trim()
            .split_whitespace()
            .map(|d| d.parse::<u32>().unwrap_or_default())
            .collect();
        // println!("{:?}", nums_in_hand);
        let nums = scratchcard_nums
            .intersection(&nums_in_hand)
            .collect::<Vec<&u32>>();
        // println!("{:?}", nums);
        if nums.len() > 0 {
            let point: u32 = 2_u32.pow(nums.len() as u32 - 1);
            points.push(point);
        }
    }
    points.into_iter().sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11";

        assert_eq!(13, solve(input));
    }
}
