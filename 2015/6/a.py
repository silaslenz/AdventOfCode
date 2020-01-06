f = open("input.txt")
instructions = f.readlines()
grid = list([0 for x in range(1000)] for y in range(1000))
for instruction in instructions:
    command = ""
    if "turn on" in instruction:
        startx,starty = instruction.split()[2].split(",")
        stopx, stopy = instruction.split()[4].split(",")
        command = "on"
    if "turn off" in instruction:
        startx, starty = instruction.split()[2].split(",")
        stopx, stopy = instruction.split()[4].split(",")
        command = "off"
    if "toggle" in instruction:
        startx, starty = instruction.split()[1].split(",")
        stopx, stopy = instruction.split()[3].split(",")
        command = "toggle"
    # print(startx,starty,stopx,stopy)
    startx = int(startx)
    starty = int(starty)
    stopx = int(stopx)
    stopy = int(stopy)
    for x in range(startx,stopx+1):
        # print(x)
        for y in range(starty,stopy+1):
            # print(y)
            # print(grid[x][y])
            if command == "on":
                grid[x][y] += 1
            if command == "off":
                grid[x][y] = max(grid[x][y]-1,0)
            if command == "toggle":
                grid[x][y] += 2
            # print(grid[x][y])
# print(grid)
count = 0
for x in range(0,1000):
    for y in range(0,1000):
            count+=grid[x][y]
print(count)