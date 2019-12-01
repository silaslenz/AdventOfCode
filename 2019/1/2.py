def get_fuel_req(weight:int):
    return weight//3-2

def get_required_extra(fuel_weight:int):
    if get_fuel_req(fuel_weight)<=0:
        return 0
    return get_required_extra(get_fuel_req(fuel_weight))+get_fuel_req(fuel_weight)

with open('input.txt') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines] 

fuel = 0
for line in lines:
    fuel+=get_fuel_req(int(line))
    fuel+=get_required_extra(get_fuel_req(int(line)))
print (fuel)
