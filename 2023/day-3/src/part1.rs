use std::usize;

type Row = Vec<char>;
type Matrix = Vec<Row>;

#[derive(Debug)]
struct EngineSchematic {
    matrix: Matrix,
    parts: Vec<u32>
}

impl EngineSchematic {
    fn new(input: &str) -> Self {
        let mut matrix: Matrix = Vec::new();
        for line in input.lines() {
            let mut row: Row = Vec::new();
            for c in line.chars() {
                row.push(c);
            }
            matrix.push(row);
        }
        EngineSchematic {matrix, parts: Vec::new()}
    }

    fn matrix_dimensions(&self) -> (usize, usize) {
        let x= self.matrix.len();
        // FIXME: don't rely on the 1st element
        let y = self.matrix[0].len();
        (x, y)
    }

    fn has_any_valid_neighbour(&self, i: usize, j: usize) -> bool {

        // top
        let (top_i, top_j) = (i - 1, j);
        // bottom
        let (bottom_i, bottom_j) = (i + 1, j);
        // left
        let (left_i, left_j) = (i, j - 1);
        // right
        let (right_i, left_j) = (i, j - 1);

        // diagonals
        // top-left
        // top-right
        // bottom-left
        // bottom-right
        true
    }

    fn find_parts(&mut self) {
        let (rows, cols) = self.matrix_dimensions();
        for i in 0..rows {
            let mut part_num: u32 = 0;
            let mut has_valid_neighbour = false;
            for j in 0..cols {
                let x: char = self.matrix[i][j];
                if x.is_digit(10) {
                    part_num = part_num * 10 + x.to_digit(10).unwrap_or_default();
                    // check if any of the neighbours are a valid symbol
                    if !has_valid_neighbour {
                        has_valid_neighbour = self.has_any_valid_neighbour(x, y);
                    }
                } else {
                    // FIXME: if num has any valid symbol as neighbours
                    // save it in the schematic part vector
                    if part_num > 0 && has_valid_neighbour {
                        self.parts.push(part_num);
                    }
                    has_valid_neighbour = false;
                    part_num = 0;
                }
            }
        }
    }
}

#[allow(dead_code)]
fn is_symbol(c: char) -> bool {
    !c.is_digit(10) && c != '.'
}

pub fn solve(input: &str) -> u32 {
    let mut p: EngineSchematic = EngineSchematic::new(input);
    p.find_parts();
    println!("{:?}", p);
    p.parts.into_iter().sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let input = "467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..";
        assert_eq!(4361, solve(input));
    }
}
