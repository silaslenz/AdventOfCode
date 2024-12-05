first_list = []
second_list = []
with open('input') as f:
    lines = f.readlines()
    for line in lines:
        a,b = line.split()
        first_list.append(int(a))
        second_list.append(int(b))

sum = 0
for a in first_list:
    print(a*second_list.count(a))
    sum+=(a*second_list.count(a))
print(sum)