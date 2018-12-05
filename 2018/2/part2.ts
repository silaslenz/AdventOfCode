const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
  input: fs.createReadStream('input'),
  crlfDelay: Infinity
});

var lines: Array<Array<number>> = [];
rl.on('line', (line) => {
  let linearray = line.split('');
  lines.push(linearray)
});

rl.on('close', () => {
    for (var i of lines){
        for (var j of lines){
            var diffs: number = 0;
            var matchingIndex: number = 0
            i.map((char, index)=>{
                if (char != j[index]){
                    diffs++;
                    matchingIndex = index;
                }
            })
            if (diffs === 1){
                i.splice(matchingIndex,1);
                console.log(i.join(''));
                process.exit(0)
            }
        }
    }
});
