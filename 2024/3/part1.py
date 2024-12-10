result = 0
with open('input') as f:
    instructions = f.read()
    potential_valid_instructions = instructions.split("mul(")
    for potential_valid_instruction in potential_valid_instructions:
        values = potential_valid_instruction.split(")")[0]
        values_split = values.split(",")
        if len(values_split)==2 and values_split[0].isdigit() and values_split[1].isdigit():
            result += int(values_split[0]) * int(values_split[1])
print(result)