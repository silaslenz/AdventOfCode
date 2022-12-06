with open("input") as file:
    lines = file.readlines()

winning_combos = (("X", "C"), ("Y", "A"), ("Z", "B"))
score = 0
for line in lines:
    opponent, me = line.split()
    if me == "X":
        score += 1
    if me == "Y":
        score += 2
    if me == "Z":
        score += 3
    if (me, opponent) in winning_combos:
        score += 6
    if me == "X" and opponent == "A" or me == "Y" and opponent == "B" or me == "Z" and opponent == "C":
        score += 3

print(score)
