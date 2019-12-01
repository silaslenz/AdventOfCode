def get_fuel_req(weight:int):
    return weight//3-2

with open('input.txt') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines] 

fuel = 0
for line in lines:
    fuel+=get_fuel_req(int(line))
print (fuel)