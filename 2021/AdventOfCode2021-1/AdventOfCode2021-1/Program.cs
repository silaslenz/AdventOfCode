using System;
using System.Collections.Generic;
using System.IO;

Console.WriteLine("Hello, World!");

var numbers = new List<int>();
foreach (string line in File.ReadLines("input"))
{
    numbers.Add(Int32.Parse(line));
}

var lastNum = Int32.MaxValue;
var numberOfIncreases = 0;
foreach (var num in numbers)
{
    if (num > lastNum)
    {
        numberOfIncreases++;
    }

    lastNum = num;
}

Console.WriteLine(numberOfIncreases);

numberOfIncreases = 0;
for (var index = 0; index < numbers.Count - 3; index++)
{
    int threeSum = numbers[index] + numbers[index + 1] + numbers[index + 2];
    int nextThreeSum = numbers[index + 1] + numbers[index + 2] + numbers[index + 3];
    if (nextThreeSum > threeSum)
    {
        numberOfIncreases++;
    }
}

Console.WriteLine(numberOfIncreases);