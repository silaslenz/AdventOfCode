// Part 2
use std::fs::File;
use std::io::{BufRead, BufReader, Result};
use std::collections::HashSet;

fn main() -> Result<()>{
    let mut sum: i32 = 0;
    let mut seen: HashSet<i32> = HashSet::new();

    let file = try!(File::open("input"));
    let input: Vec<i32>  = BufReader::new(file).lines().map(|line| line.unwrap().parse::<i32>().unwrap()).collect();

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