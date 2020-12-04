import sys

with open("input",'r') as file:
    lines = [int(x) for x in file.read().splitlines()]

for line in lines:
    for line2 in lines:
        if line+line2 == 2020:
            print(line*line2)
            sys.exit(0)