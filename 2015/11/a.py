import sys
input = "cqjxjnds"

index = 0

for changeindex  in range(len(input)-1,0,-1):
    while True:
        if (input[changeindex]) =='z':
            tmp = list(input)

            tmp[changeindex] = 'a'
            input = ''.join(tmp)
            break
        else:
            tmp = list(input)

            tmp[changeindex] = chr(ord(input[changeindex])+1)
            input = ''.join(tmp)
        # print(input)

        ok = False
        if 'i' in input or 'o' in input or 'l' in input:
            continue
        index = 0
        while index < len(input)-2:
            if ord(input[index]) + 2 == ord(input[index + 1]) == ord(input[index+2]):
                ok = True
            index += 1
        if not ok:
            continue
        print(input)

        found = 0
        for letter in "abcdefghijklmnopqrstuvwxyz":
            if input.count(letter+letter):
                found+=input.count(letter+letter)
        # print(found)
        if found>0:
            print(input)
            sys.exit()