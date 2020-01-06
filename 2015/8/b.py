f = open("input.txt")
strings = f.readlines()
count = 0

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

for string in strings:
    string = string.rstrip()
    # print(string)
    origlen = len(string)
    # string = string[1:len(string) - 1]
    # print(string)
    # print(string)
    string = string.replace('\\', '\\\\')
    string = string.replace('"', '\\"')
    # print(string)
    print(string)
    stringlen = len(string)+2
    # blabla = list(find_all(string,"\\x"))
    # for bla in blabla:
    #     try:
    #         int(string[bla+2:bla+4],16)
    #         stringlen -= 3
    #     except:
    #         pass



    print(origlen,stringlen)
    count +=  stringlen-origlen
print(count)
