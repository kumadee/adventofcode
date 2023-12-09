use std::collections::HashSet;

pub fn solve(input: &str) -> u32 {
    let total_card_num = input.lines().count();
    let mut scratchcards: Vec<u32> = vec![0; total_card_num];
    for (card_num, line) in input.lines().enumerate() {
        let colon_idx = match line.find(":") {
            Some(c) => c,
            None => 0,
        };
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
        let nums_in_hand: HashSet<u32> = line[pipe_idx..]
            .trim()
            .split_whitespace()
            .map(|d| d.parse::<u32>().unwrap_or_default())
            .collect();
        let nums = scratchcard_nums
            .intersection(&nums_in_hand)
            .collect::<Vec<&u32>>();

        if nums.len() > 0 {
            scratchcards[card_num] = nums.len().try_into().unwrap_or_default();
        }
    }
    calc_total_scratchcards(&scratchcards)
}

// 1 -> 4 -> 1 + 0 = done
// 2 -> 2 -> 1 + 1 + 0 = done
// 3 -> 2 -> 1 + 1 + 2 + 0 = done
// 4 -> 1 -> 1 + 1 + 2 + 4 + 0 = done
// 5 -> 0 -> 1 + 1 + 4 + 8 + 0 = done
// 6 -> 0 -> 1 + 0 = done
// 1 + 2 + 4 + 8 + 14 + 1 = 30
fn calc_total_scratchcards(points: &Vec<u32>) -> u32 {
    let count = points.len();
    let mut card_count = vec![1_u32; count];
    for (i, p) in points.into_iter().enumerate() {
        // println!("card {}, count: {}", i + 1, card_count[i]);
        if i + 1 >= count {
            break;
        }
        let mut j: usize = i + <u32 as TryInto<usize>>::try_into(*p).unwrap();
        if j > count {
            j = count - 1;
        }
        for x in i + 1..=j {
            card_count[x] += card_count[i];
            // println!("=> card {}, count: {}", x + 1, card_count[x]);
        }
    }
    // println!("card_count: {:?}", card_count);
    card_count.into_iter().sum()
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

        assert_eq!(30, solve(input));
    }
}
