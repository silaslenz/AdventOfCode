def evaluate_safety(levels):
    last = levels[0]
    increasing = levels[1] - levels[0] > 0
    for level in levels[1:]:
        if (increasing and level < last) or (not increasing and level > last):
            return True
        if (not (1 <= abs(level - last) <= 3)):
            return True
        last = level
    return False


if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()
        safe = 0
        for line in lines:
            levels = [int(x) for x in line.split()]
            unsafe = evaluate_safety(levels)
            if not unsafe:
                safe += 1
        print(safe)
