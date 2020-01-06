f = open("input.txt")
presents = f.readlines()
total = 0
for present in presents:
    l,w,h = [int(x) for x in present.split("x")]
    sidea = l*w
    sideb = w*h
    sidec = h*l
    area  = 2*sidea+2*sideb+2*sidec + min(sideb,sidec,sidea)

    total += area
print(total)