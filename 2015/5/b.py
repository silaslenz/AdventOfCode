f = open("input.txt")
strings = f.readlines()
count = 0
def repeats(string):
    for x in range(0,len(string)-2):
        substring = string[x:x+2]
        if string.count(substring)>1:
            return True
    return False



for string in strings:
    if repeats(string):
        for x in range(0,len(string)-2):
            if string[x] == string[x+2]:
                count+=1
                break
print(count)