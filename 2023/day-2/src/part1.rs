#[derive(Debug)]
pub struct Cube {
    red: u16,
    green: u16,
    blue: u16,
}

impl Cube {
    pub fn new(red: u16, green: u16, blue: u16) -> Cube {
        Cube { red, green, blue }
    }
}

#[derive(Debug)]
struct Game {
    id: u32,
    cube: Cube,
    cubes: Vec<Cube>,
}

fn parse_set(set: &str) -> Cube {
    let mut cube = Cube::new(0, 0, 0);
    for c in set.split(",") {
        if let Some((count, color)) = c.trim().split_once(' ') {
            let count = count.parse().unwrap();
            match color {
                "red" => {
                    cube.red = count;
                }
                "green" => {
                    cube.green = count;
                }
                "blue" => {
                    cube.blue = count;
                }
                _ => (),
            }
        }
    }
    cube
}

fn game_total_cube(line: &str) -> Game {
    let mut game = Game {
        id: 0,
        cube: Cube::new(0, 0, 0),
        cubes: vec![],
    };

    let mut id = String::from("");
    for c in line.chars() {
        if c == ':' {
            break;
        }
        if c.is_digit(10) {
            id.push(c);
        }
    }
    game.id = id.parse().unwrap();
    let prefix = format!("Game {}:", id);
    if let Some(sets) = line.strip_prefix(&prefix) {
        let cubes: Vec<Cube> = sets.split(";").map(|set| parse_set(set)).collect();
        for c in &cubes {
            game.cube.red += c.red;
            game.cube.green += c.green;
            game.cube.blue += c.blue;
        }
        game.cubes = cubes;
    };
    game
}

fn is_allowed(game: &Game, allowed_cube: &Cube) -> bool {
    let mut res = false;
    for c in &game.cubes {
        res = c.red <= allowed_cube.red
            && c.green <= allowed_cube.green
            && c.blue <= allowed_cube.blue;
        if !res {
            return false;
        }
    }
    res
}

pub fn solve(input: &str, allowed_cube: &Cube) -> u32 {
    input
        .lines()
        .map(|game| game_total_cube(game.trim_start()))
        .filter_map(|g| match is_allowed(&g, allowed_cube) {
            true => Some(g.id),
            false => None,
        })
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";
        let allowed_cube = Cube::new(12, 13, 14);
        assert_eq!(8, solve(input, &allowed_cube));
    }
}
