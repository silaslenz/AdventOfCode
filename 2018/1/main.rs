// Part 1
use std::fs::File;
use std::io::{BufRead, BufReader, Result};


fn main() -> Result<()>{
    let file = try!(File::open("input"));
    let sum: i32 = BufReader::new(file).lines().map(|line| line.unwrap().parse::<i32>().unwrap()).sum();
    println!("Final sum {}", sum);
    Ok(())
}