with open("input",'r') as file:
    lines = file.read().splitlines()

def parse_line(line):
    count, letter, password = line.split(" ")
    minimum, maximum = count.split("-")
    minimum=int(minimum)
    maximum=int(maximum)
    letter = letter.split(":")[0]
    return minimum,maximum,letter,password

valid = 0
for line in lines:
    minimum,maximum,letter,password = parse_line(line)
    if minimum<=password.count(letter)<=maximum:
        valid+=1
print(valid)

valid = 0
for line in lines:
    minimum,maximum,letter,password = parse_line(line)
    if password[minimum-1] == letter and password[maximum-1]!=letter or password[minimum-1] != letter and password[maximum-1]==letter:
        valid+=1
print(valid)