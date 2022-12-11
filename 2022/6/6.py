with open("input") as file:
    line = file.readline()
chars = 4  # Replace with 14 for part 2
for x in range(0, len(line) - (chars - 1)):
    if len(set(line[x:x + chars])) == chars:
        print(line[x:x + chars], x + chars)
        break
