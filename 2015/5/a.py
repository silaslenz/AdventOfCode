f = open("input.txt")
strings = f.readlines()
count = 0
for string in strings:
    if "ab" in string or "cd" in string or "pq" in string or "xy" in string:
        continue
    if string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u") < 3:
        continue
    for letter in "abcdefghijklmnopqrstuvwxyz":

        if string.count(letter+letter)>=1:
            count+=1
            break


print(count)