use std::usize;

type Row = Vec<char>;
type Vec2d = Vec<Row>;

#[derive(Debug)]
struct Matrix {
    data: Vec2d,
    dimensions: (usize, usize),
}

impl Matrix {
    fn new(input: &str) -> Self {
        let mut matrix: Vec2d = Vec::new();
        for line in input.lines() {
            let mut row: Row = Vec::new();
            for c in line.trim_start().chars() {
                row.push(c);
            }
            matrix.push(row);
        }
        // Assumption, all rows are same length as 0th row
        let (x, y) = (matrix.len(), matrix[0].len());
        Matrix {
            data: matrix,
            dimensions: (x, y),
        }
    }

    fn is_symbol(&self, i: usize, j: usize) -> bool {
        let c: char = self.data[i][j];
        !c.is_digit(10) && c != '.'
    }

    fn has_any_valid_neighbour(&self, i: usize, j: usize) -> bool {
        let (m_x, m_y) = self.dimensions;
        // top
        if i > 0 && self.is_symbol(i - 1, j) {
            return true;
        }
        // bottom
        if i < m_x - 1 && self.is_symbol(i + 1, j) {
            return true;
        }
        // left
        if j > 0 && self.is_symbol(i, j - 1) {
            return true;
        }
        // right
        if j < m_y - 1 && self.is_symbol(i, j + 1) {
            return true;
        }

        // diagonals
        // top-left
        if i > 0 && j > 0 && self.is_symbol(i - 1, j - 1) {
            return true;
        }
        // top-right
        if i > 0 && j < m_y - 1 && self.is_symbol(i - 1, j + 1) {
            return true;
        }
        // bottom-left
        if i < m_x - 1 && j > 0 && self.is_symbol(i + 1, j - 1) {
            return true;
        }
        // bottom-right
        if i < m_x - 1 && j < m_y - 1 && self.is_symbol(i + 1, j + 1) {
            return true;
        }

        // Equivalent to above, but requires many type-casting operations
        // for (rr, cc) in vec![
        //     (-1, 0),  // top
        //     (1, 0),   // bottom
        //     (0, -1),  // left
        //     (0, 1),   // right
        //     (-1, -1), // top-left
        //     (-1, 1),  // top-right
        //     (1, -1),  // bottom-left
        //     (1, 1),   // bottom-right
        // ] {
        //     let x = i as i32 + rr;
        //     let y = j as i32 + cc;
        //     if 0 <= x && x < (m_x - 1) as i32 && 0 <= y && y <= (m_y - 1) as i32 {
        //         if self.is_symbol(x as usize, y as usize) {
        //             return true;
        //         }
        //     }
        // }
        false
    }
}

#[derive(Debug)]
struct EngineSchematic {
    matrix: Matrix,
    parts: Vec<u32>,
}

impl EngineSchematic {
    fn new(input: &str) -> Self {
        let matrix: Matrix = Matrix::new(input);
        EngineSchematic {
            matrix,
            parts: Vec::new(),
        }
    }

    fn find_parts(&mut self) {
        let (rows, cols) = self.matrix.dimensions;
        for i in 0..rows {
            let mut part_num: u32 = 0;
            let mut has_valid_neighbour = false;
            // let mut invalids: Vec<u32> = Vec::new();
            // let mut valids: Vec<u32> = Vec::new();
            for j in 0..cols {
                let ch: char = self.matrix.data[i][j];
                let is_digit = ch.is_digit(10);
                if is_digit {
                    part_num = part_num * 10 + ch.to_digit(10).unwrap();
                    // check if any of the neighbours is a valid symbol
                    if !has_valid_neighbour {
                        has_valid_neighbour = self.matrix.has_any_valid_neighbour(i, j);
                    }
                }
                // if no longer a digit or last element on the line
                if !is_digit || j+1 == cols {
                    // if num has any valid symbol as neighbours
                    // save it in the schematic part vector
                    if part_num > 0 && has_valid_neighbour {
                        self.parts.push(part_num);
                        // valids.push(part_num);
                    }
                    // if part_num > 0 && !has_valid_neighbour {
                    //     invalids.push(part_num);
                    // }
                    has_valid_neighbour = false;
                    part_num = 0;
                }
            }
            // if invalids.len() > 0 {
            //     println!("line {}, invalids {:?}", i + 1, invalids);
            // }
            // println!(
            //     "line {}, valids {:?}, sum {}",
            //     i + 1,
            //     valids,
            //     (&valids).into_iter().sum::<u32>()
            // );
        }
    }
}

pub fn solve(input: &str) -> u32 {
    let mut engine: EngineSchematic = EngineSchematic::new(input);
    engine.find_parts();
    engine.parts.into_iter().sum()
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
