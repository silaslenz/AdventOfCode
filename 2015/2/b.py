f = open("input.txt")
presents = f.readlines()
total = 0
for present in presents:
    l,w,h = [int(x) for x in present.split("x")]
    length = l*w*h
    length += sorted([l,w,h])[0]*2
    length += sorted([l, w, h])[1] * 2


    total += length
print(total)