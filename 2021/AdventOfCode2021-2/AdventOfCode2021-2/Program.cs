// See https://aka.ms/new-console-template for more information


using System;

var numbers = new List<int>();
var position = new Point();
foreach (string line in File.ReadLines("input"))
{
    var split_line = line.Split(" ");
    switch (split_line[0])
    {
        case "forward":
            position.Horizontal+=int.Parse(split_line[1]);
            break;
        case "down":
            position.Depth+=int.Parse(split_line[1]);
            break;
        case "up":
            position.Depth-=int.Parse(split_line[1]);
            break;
    }
}
Console.WriteLine($"{position.Depth} {position.Horizontal}");
Console.WriteLine(position.Depth*position.Horizontal);

position.Horizontal = 0;
position.Depth = 0;
foreach (string line in File.ReadLines("input"))
{
    var split_line = line.Split(" ");
    switch (split_line[0])
    {
        case "forward":
            position.Horizontal+=int.Parse(split_line[1]);
            position.Depth+=(int.Parse(split_line[1])*position.Aim);
            break;
        case "down":
            position.Aim += int.Parse(split_line[1]);
            break;
        case "up":
            position.Aim -= int.Parse(split_line[1]);
            break;
    }
}
Console.WriteLine($"{position.Depth} {position.Horizontal}");
Console.WriteLine(position.Depth*position.Horizontal);
public struct Point
{
    public int Horizontal{ get; set; }
    public int Depth { get; set; }
    public int Aim { get; set; }
};