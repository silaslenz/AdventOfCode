f = open("input.txt")
directions = f.read()
x, y = 0, 0
robox, roboy = 0, 0
locations = set()
index = 0
while index<len(directions):
    direction = directions[index]
    if direction == ">":
        y += 1
    if direction == "<":
        y -= 1
    if direction == "^":
        x += 1
    if direction == "v":
        x -= 1
    index+=1
    locations.add((x,y))

    direction2 = directions[index]
    if direction2 == ">":
        roboy += 1
    if direction2 == "<":
        roboy -= 1
    if direction2 == "^":
        robox += 1
    if direction2 == "v":
        robox -= 1
    index += 1
    locations.add((robox,roboy))
print(len(locations))
