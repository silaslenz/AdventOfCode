distribution = [int(x) for x in "4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3".split()]
#distribution = [int(x) for x in "0 2 7 0".split()]
print(distribution)

configurations = []
def find_max(banks):
    max_bank = 0
    max_index = 0
    for bank_index in range(len(banks)):
        if banks[bank_index]>max_bank:
            max_bank = banks[bank_index]
            max_index = bank_index
    return max_index

def spread_out(banks, num, max_index):
    distribution[max_index] = 0
    if max_index < len(banks) - 1:
        index = max_index + 1
    else:
        index = 0
    while num>0:
        banks[index] += 1
        num -= 1
        if index < len(banks) - 1:
            index += 1
        else:
            index = 0
    return banks
print(find_max(distribution))


while len(set(configurations)) == len(configurations):
    str_distribution = [str(x) for x in distribution]
    configurations.append(','.join(str_distribution))
    distribution = spread_out(distribution, distribution[find_max(distribution)], find_max(distribution))
print(configurations)
print(len(configurations)-1)