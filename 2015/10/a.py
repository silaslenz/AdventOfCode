from collections import OrderedDict

input = "1321131112"
for i in range(50):
    next = ""
    index = 0
    while index < len(input):
        # print(input,index)
        j = input[index]
        c = 0
        while True:
            try:
                if input[index] == j:
                    c += 1
                    index += 1
                else:
                    break
            except:
                break
        if c != 0:
            next += str(c) + str(j)
    input = next
print(len(next))
