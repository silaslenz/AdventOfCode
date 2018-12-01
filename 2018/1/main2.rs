// Part 2
use std::fs::File;
use std::io::{BufRead, BufReader, Result};
use std::collections::HashSet;

fn main() -> Result<()>{
    let mut sum: i32 = 0;
    let mut seen: HashSet<i32> = HashSet::new();
    let mut input: Vec<i32> = Vec::new();

    let file = try!(File::open("input"));
    for line in BufReader::new(file).lines() {
        input.push(line.unwrap().parse().unwrap());
    }

    'outer: loop{
        for number in &input{
            sum+=number;
            if seen.contains(&sum){
                println!("Seen first frequency twice! {}", sum);
                break 'outer;
            }
            seen.insert(sum);
        }
    }
    println!("Final sum {}", sum);
    Ok(())
}