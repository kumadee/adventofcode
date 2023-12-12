use std::collections::HashMap;

type MyMap = Vec<Data>;

struct Data {
    dest: u64,
    src: u64,
    length: u64,
}

fn get(my_map: &MyMap, src_key: u64) -> Option<u64> {
    for data in my_map {
        let diff = src_key - data.src;
        if src_key < data.src && diff < data.length {
            return Some(data.dest + diff);
        }
    }
    None
}

pub fn solve(input: &str) -> u64 {
    let seed_to_soil: MyMap = Vec::new();
    let soil_to_fertilizer: MyMap = Vec::new();
    let fertilizer_to_water: MyMap = Vec::new();
    let water_to_light: MyMap = Vec::new();
    let light_to_temp: MyMap = Vec::new();
    let temp_to_humidity: MyMap = Vec::new();
    let humidity_to_location: MyMap = Vec::new();
    let mut seeds: Vec<u64> = Vec::new();

    for line in input.lines() {
        if line.starts_with("seeds:") {
            seeds = line[6..]
            .split_whitespace()
            .map(|d| d.parse::<u64>().unwrap_or_default())
            .collect();
        }

        if line.starts_with("seed-to-soil map:") {

        }
    }

    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let input = "
        seeds: 79 14 55 13

        seed-to-soil map:
        50 98 2
        52 50 48
        
        soil-to-fertilizer map:
        0 15 37
        37 52 2
        39 0 15
        
        fertilizer-to-water map:
        49 53 8
        0 11 42
        42 0 7
        57 7 4
        
        water-to-light map:
        88 18 7
        18 25 70
        
        light-to-temperature map:
        45 77 23
        81 45 19
        68 64 13
        
        temperature-to-humidity map:
        0 69 1
        1 0 69
        
        humidity-to-location map:
        60 56 37
        56 93 4";

        assert_eq!(35, solve(input));
    }
}
