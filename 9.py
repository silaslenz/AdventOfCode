file = open("9.input", "r") 
stream = file.readline()


score = 0
depth = 0
in_garbage = False
escapechar = False
garbagescore = 0

for c in stream:
    if in_garbage:
        if escapechar:
            escapechar = False
        elif c == "!":
            escapechar = True
        elif c == ">":
            in_garbage = False
        else:
            garbagescore += 1
        
    else:
        if c == "{":
            depth += 1
        elif c == "}":
            score += depth
            depth -= 1
        elif c == "<":
            in_garbage = True

print(score)
print(garbagescore)