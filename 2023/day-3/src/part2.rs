use std::{usize, collections::HashMap};

type Row = Vec<char>;
type Vec2d = Vec<Row>;
type Gear = (usize, usize);

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

    fn is_gear_symbol(&self, i: usize, j: usize) -> bool {
        let c: char = self.data[i][j];
        c == '*'
    }

    fn has_valid_gear_neighbour(&self, i: usize, j: usize) -> (bool, Gear) {
        let (m_x, m_y) = self.dimensions;

        for (rr, cc) in vec![
            (-1, 0),  // top
            (1, 0),   // bottom
            (0, -1),  // left
            (0, 1),   // right
            (-1, -1), // top-left
            (-1, 1),  // top-right
            (1, -1),  // bottom-left
            (1, 1),   // bottom-right
        ] {
            let x = i as i32 + rr;
            let y = j as i32 + cc;
            if 0 <= x && x < (m_x - 1) as i32 && 0 <= y && y <= (m_y - 1) as i32 {
                if self.is_gear_symbol(x as usize, y as usize) {
                    return (true, (x as usize, y as usize));
                }
            }
        }
        (false, (0, 0))
    }
}

#[derive(Debug)]
struct GearPart {
    num: u32,
    gear_location: Gear,
}

impl GearPart {
    fn new(num: u32, gear_location: Gear) -> Self {
        GearPart { num, gear_location }
    }
}

#[derive(Debug)]
struct EngineSchematic {
    matrix: Matrix,
    parts: Vec<GearPart>,
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
            let mut gear_location: Gear = (0, 0);
            for j in 0..cols {
                let ch: char = self.matrix.data[i][j];
                let is_digit = ch.is_digit(10);
                if is_digit {
                    part_num = part_num * 10 + ch.to_digit(10).unwrap();
                    // check if any of the neighbours is a valid symbol
                    if !has_valid_neighbour {
                        (has_valid_neighbour, gear_location) = self.matrix.has_valid_gear_neighbour(i, j);
                    }
                }
                // if no longer a digit or last element on the line
                if !is_digit || j+1 == cols {
                    // if num has a gear symbol as neighbour
                    // save it in the schematic part vector
                    if part_num > 0 && has_valid_neighbour {
                        let g = GearPart::new(part_num, gear_location);
                        self.parts.push(g);
                    }

                    has_valid_neighbour = false;
                    part_num = 0;
                }
            }
        }
    }

    fn calculate_gear_ratios(&self) -> Vec<u32> {
        let mut map: HashMap<Gear, u32> = HashMap::new();
        let mut ratios: Vec<u32> = Vec::new();
        for part in &self.parts {
            if let Some(p) = map.get(&part.gear_location) {
                let r = *p * part.num;
                ratios.push(r);
                map.remove(&part.gear_location);
            } else {
                map.insert(part.gear_location, part.num);
            }
        }
        ratios
    }
}

pub fn solve(input: &str) -> u32 {
    let mut engine: EngineSchematic = EngineSchematic::new(input);
    engine.find_parts();
    engine.calculate_gear_ratios().into_iter().sum()
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
        assert_eq!(467835, solve(input));
    }
}
