f = open("input.txt")
outputs = {}
instructions = f.readlines()
for instruction in instructions:
    input, output = instruction.split("->")
    outputs[output.strip()] = input
print(outputs)


def solve(want):
    global outputs
    if want.isdigit():
        print("yay")
        return int(want)
    print("want", want)
    if type(outputs[want])==int:
        print("yay", outputs[want])
        return int(outputs[want])
    print("commands are", outputs[want])
    if len(outputs[want].split()) == 1:
        print("WTF")
        return solve(outputs[want].strip())
    elif len(outputs[want].split()) == 3:
        a, operation, b = outputs[want].strip().split()
        # print(a,b,operation)
        if a.isdigit() and b.isdigit():
            a, b = int(a), int(b)
        else:
            if a.isdigit():
                b = solve(b.strip())
                a = int(a)
            elif b.isdigit():
                a = solve(a.strip())
                b = int(b)
            else:
                a = solve(a.strip())
                b = solve(b.strip())
        # print(a,b)
        if operation == "AND":
            outputs[want] = (a & b)&0xFFFF
            return (int(a) & int(b))&0xFFFF
        if operation == "OR":
            outputs[want] = (a | b)&0xFFFF
            return (int(a) | int(b))&0xFFFF
        if operation == "LSHIFT":
            outputs[want] = (a << b)&0xFFFF
            return (int(a) << int(b))&0xFFFF
        if operation == "RSHIFT":
            outputs[want] = (a >> b)&0xFFFF
            return (int(a) >> int(b))&0xFFFF
    else:
        operation, b = outputs[want].strip().split()
        if b.isdigit():
            b = int(b)
        else:
            b = solve(b)
        outputs[want] = ~int(b) & 0xFFFF
        return ~int(b) & 0xFFFF
outputs = {}
# instructions = f.readlines()
for instruction in instructions:
    input, output = instruction.split("->")
    outputs[output.strip()] = input
print(outputs)


outputs['b'] = 956
print(solve('a'))
