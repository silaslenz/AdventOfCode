first_list = []
second_list = []
with open('input') as f:
    lines = f.readlines()
    for line in lines:
        a,b = line.split()
        first_list.append(int(a))
        second_list.append(int(b))

sum = 0
for a, b in zip(sorted(first_list), sorted(second_list)):
    sum+=(abs(a-b))
print(sum)