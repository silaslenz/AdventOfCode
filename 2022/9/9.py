with open("input") as f:
    lines = f.readlines()

location = [[0, 0] for _ in range(2)]  # Change to 10 for part 2
max_x = 5
max_y = 5
min_x = 0
min_y = 0
tail_touched = set()


def divide_by_two_and_round_away_from_zero(value: int):
    return value // 2 if value * 2 < 0 else (value + (-value % 2)) // 2


for line in lines:
    direction, distance = line[0], int(line[1:])

    for _ in range(distance):
        # print(line.strip())
        tail_touched.add(tuple(location[-1]))

        match direction:
            case "R":
                location[0] = (location[0][0] + 1, location[0][1])
            case "L":
                location[0] = (location[0][0] - 1, location[0][1])
            case "U":
                location[0] = (location[0][0], location[0][1] + 1)
            case "D":
                location[0] = (location[0][0], location[0][1] - 1)

        for i in range(1, len(location)):
            if (location[i - 1][0] == location[i][0]) and (location[i - 1][1] == location[i][1]):
                pass
                # print("Head covers tail")
            elif (abs(location[i - 1][0] - location[i][0]) + abs(location[i - 1][1] - location[i][1]) == 1) or (
                    abs(location[i - 1][0] - location[i][0]) == 1 and abs(location[i - 1][1] - location[i][1]) == 1):
                pass
                # print("Head touches tail")
            elif abs(location[i - 1][0] - location[i][0]) == 2 and location[i - 1][1] == location[i][1]:
                # print("Head is 2 away from tail in x")
                location[i][0] = location[i][0] + (location[i - 1][0] - location[i][0]) // 2
            elif abs(location[i - 1][1] - location[i][1]) == 2 and location[i - 1][0] == location[i][0]:
                # print("Head is 2 away from tail in y")
                location[i][1] = location[i][1] + (location[i - 1][1] - location[i][1]) // 2
            elif (location[i - 1][0] - location[i][0]) != 0 and (location[i - 1][1] - location[i][1]) != 0:
                # print("Not in same row or column")
                diff_x = location[i - 1][0] - location[i][0]
                location[i][0] = location[i][0] + divide_by_two_and_round_away_from_zero(diff_x)
                diff_y = location[i - 1][1] - location[i][1]
                location[i][1] = location[i][1] + divide_by_two_and_round_away_from_zero(diff_y)
        tail_touched.add(tuple(location[-1]))

        max_x = max(max_x, max([x[0] for x in location]))
        max_y = max(max_y, max([x[1] for x in location]))
        min_x = min(min_x, min([x[0] for x in location]))
        min_y = min(min_y, min([x[1] for x in location]))

for (x, y) in [(x, y) for y in range(min_y, max_y + 1) for x in range(min_x, max_x + 1)]:
    if (x, y) in tail_touched:
        print("x", end="" if x != max_x else "\n")
    else:
        print(".", end="" if x != max_x else "\n")

print(len(tail_touched))
