from pprint import pprint
grid = [[0 for x in range(20)] for y in range(20)] 
sumgrid = [[0 for x in range(20)] for y in range(20)] 
sumgrid[-10][-10] = 1
target = 100
dx, dy = 0, -1
x, y = 0, 0
for index in range(target - 1):
    grid[y-10][x-10] = index + 1
    if y!=0 or x!=0:
        sumgrid[y-10][x-10] = sumgrid[y-11][x-11] + sumgrid[y-11][x-10] + sumgrid[y-11][x-9] + sumgrid[y-10][x-9] + sumgrid[y-10][x-11] + sumgrid[y-9][x-11] + sumgrid[y-9][x-10] + sumgrid[y-9][x-9]
        if sumgrid[y-10][x-10] >= 289326:
            print("kdlasjdlkasjdlkasjdlkasjlkd", sumgrid[y-10][x-10])
    if x == y or (x < 0 and y == -x) or (x > 0 and x == 1 - y):
        print("flip at", x, y)
        dx, dy = -dy, dx
        print(dx,dy)
    x += dx
    y += dy

pprint(grid)
pprint(sumgrid)
print (x,y)
distance = abs(0 - x) + abs(0 - y)

print(distance)