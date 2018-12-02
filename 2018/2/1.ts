const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: fs.createReadStream('input'),
  crlfDelay: Infinity
});

function has_duplicate(arr: Array<number>, duplicates: number){
    return arr.filter((a,i,b) =>
          arr.filter(v => v===a).length === duplicates
    ).length !== 0;
}

var c1: number = 0;
var c2: number = 0;
rl.on('line', (line) => {
  let linearray = line.split('');
  if(has_duplicate(linearray,2)){
    c1++;
  }
  if(has_duplicate(linearray, 3)){
    c2++;
  }
});

rl.on('close', () => {
    console.log(c1*c2);
});
