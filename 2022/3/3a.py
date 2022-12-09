with open("input") as file:
    data = file.read().splitlines()

alphabeth = "abcdefghijklmnopqrstuvwxyz"
points = 0
for line in data:
    compartment_a, compartment_b = set(line[len(line) // 2:]), set(line[:len(line) // 2])
    duplicates = compartment_a.intersection(compartment_b)
    for duplicate in duplicates:
        if duplicate.islower():
            points += alphabeth.index(duplicate) + 1
        else:
            points += alphabeth.index(duplicate.lower()) + 27
print(points)