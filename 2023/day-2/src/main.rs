use std::env;
use std::fs;

mod part1;
mod part2;

use part1::Cube;

fn main() {
    let args: Vec<String> = env::args().collect();

    let file_path = &args[1];

    println!("In file {}", file_path);

    let contents = fs::read_to_string(file_path).expect("Should have been able to read the file");
    let allowed_cube  = Cube::new(12, 13, 14);
    println!("Part 1 - Sum: {}", part1::solve(&contents, &allowed_cube));
    println!("Part 2 - Sum: {}", part2::solve(&contents));
}
