# Part 1
instructions = """set b 57
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23
"""
def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

registers = {"a" : 1, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}
mulcounter = 0


def do_set(x,y):
    if is_int(y):
        registers[x] = int(y)
    else:
        registers[x] = registers[y]

def do_sub(x,y):
    if is_int(y):
        registers[x] -= int(y)
    else:
        registers[x] -= registers[y]

def do_mul(x,y):
    global mulcounter
    mulcounter += 1
    if is_int(y):
        registers[x] *= int(y)
    else:
        registers[x] *= registers[y]

def do_jnz(x,y):
    if is_int(x):
        if int(x) == 0:
            return 1
        else:
            return int(y)
    else:
        if registers[x] == 0:
            return 1
        else:
            return int(y)

def do_instruction(instruction):
    
    instruction, parameter1, parameter2 = instruction.split()
    nextjump = 1
    if instruction == "set":
        do_set(parameter1, parameter2)
    if instruction == "sub":
        do_sub(parameter1, parameter2)
    if instruction == "mul":
        do_mul(parameter1, parameter2)
    if instruction == "jnz":
        nextjump = do_jnz(parameter1, parameter2)
    return nextjump

instructionpointer = 0

while instructionpointer<len(instructions.splitlines()):
    #print(instructionpointer)
    instructionpointer += do_instruction(instructions.splitlines()[instructionpointer])
    #print(registers)

print(mulcounter)