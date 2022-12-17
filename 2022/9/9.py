import math

with open("input") as f:
    lines = f.readlines()

location_head = (0, 0)
location_tail = [0, 0]
max_x = 5
max_y = 5
tail_touched = set()
for line in lines:
    direction, distance = line[0], int(line[1:])

    for _ in range(distance):
        print(line.strip())
        tail_touched.add(tuple(location_tail))


        if direction == "R":
            location_head = (location_head[0] + 1, location_head[1])
        elif direction == "L":
            location_head = (location_head[0] - 1, location_head[1])
        elif direction == "U":
            location_head = (location_head[0], location_head[1] + 1)
        elif direction == "D":
            location_head = (location_head[0], location_head[1] - 1)

        if (location_head[0] == location_tail[0]) and (location_head[1] == location_tail[1]):
            print("Head covers tail")
        elif (abs(location_head[0] - location_tail[0]) + abs(location_head[1] - location_tail[1]) == 1) or (
                abs(location_head[0] - location_tail[0]) == 1 and abs(location_head[1] - location_tail[1]) == 1):
            print("Head touches tail")
        elif abs(location_head[0] - location_tail[0]) == 2 and location_head[1] == location_tail[1]:
            print("Head is 2 away from tail in x")
            location_tail[0] = location_tail[0] + (location_head[0] - location_tail[0]) // 2
        elif abs(location_head[1] - location_tail[1]) == 2 and location_head[0] == location_tail[0]:
            print("Head is 2 away from tail in y")
            location_tail[1] = location_tail[1] + (location_head[1] - location_tail[1]) // 2
        elif (location_head[0] - location_tail[0]) != 0 and (location_head[1] - location_tail[1]) != 0:
            print("Not in same row or column")
            a_x = location_head[0] - location_tail[0]
            b = 2
            location_tail[0] = location_tail[0] + (a_x // b if a_x * b < 0 else (a_x + (-a_x % b)) // b)
            a_y = location_head[1] - location_tail[1]
            location_tail[1] = location_tail[1] + (a_y // b if a_y * b < 0 else (a_y + (-a_y % b)) // b)
        tail_touched.add(tuple(location_tail))

        max_x = max(max_x, location_head[0], location_tail[0])
        max_y = max(max_y, location_head[1], location_tail[1])
        for (x, y) in [(x, y) for y in range(max_y + 1) for x in range(max_x + 1)]:
            if (x, y) == location_head:
                print("H", end="" if x != max_x else "\n")
            elif (x, y) == tuple(location_tail):
                print("T", end="" if x != max_x else "\n")
            else:
                print(".", end="" if x != max_x else "\n")
print(len(tail_touched))