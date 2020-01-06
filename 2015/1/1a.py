f = open("input.txt")
text = f.read()
level = 0
index = 1
while index<len(text):
    if text[index - 1] == "(":
        level += 1
    if text[index - 1] == ")":
        level -= 1
    if level == -1:
        print(index)
    index += 1
a = text.count("(")
b = text.count(")")
print(a - b)
