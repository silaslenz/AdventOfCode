with open("input") as file:
    lines = file.readlines()

winning_combos = {"A": "B", "B": "C", "C": "A"}
loosing_combos = {"A": "C", "B": "A", "C": "B"}
score = 0
for line in lines:
    opponent, wanted = line.split()
    if wanted == "X":
        # Loose
        score += 0
        me = loosing_combos[opponent]
    if wanted == "Y":
        # Draw
        score += 3
        me = opponent
    if wanted == "Z":
        # Win
        score += 6
        me = winning_combos[opponent]
    if me == "A":
        score += 1
    if me == "B":
        score += 2
    if me == "C":
        score += 3

print(score)
