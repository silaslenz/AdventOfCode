// Part 1
use std::fs::File;
use std::io::{BufRead, BufReader, Result};


fn main() -> Result<()>{
    let mut sum: i32 = 0;
    let file = try!(File::open("input"));
    for line in BufReader::new(file).lines() {
        let number: i32 = line.unwrap().parse().unwrap();
        sum+=number;
        println!("{}", number);
    }
    println!("Final sum {}", sum);
    Ok(())
}