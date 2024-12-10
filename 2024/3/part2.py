import re
result = 0
with open('input') as f:
    instructions = f.read()
    real_instructions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", instructions)
    disable = False
    for real_instruction in real_instructions:
        if real_instruction == "do()":
            disable = False
            continue
        if real_instruction == "don't()":
            disable = True
            continue
        if disable:
            continue
        print(real_instruction)
        values = real_instruction.split(",")
        result += int(values[0][4:]) * int(values[1][:-1])

print(result)