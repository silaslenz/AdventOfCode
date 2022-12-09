with open("input") as file:
    data = file.read().splitlines()

alphabeth = "abcdefghijklmnopqrstuvwxyz"
points = 0
for i in range(0, len(data), 3):
    group_a, group_b, group_c = set(data[i]), set(data[i + 1]), set(data[i + 2])
    duplicate = list(group_a.intersection(group_b, group_c))[0]
    if duplicate.islower():
        points += alphabeth.index(duplicate) + 1
    else:
        points += alphabeth.index(duplicate.lower()) + 27
print(points)