from collections import defaultdict
from itertools import accumulate
from pathlib import Path

with open("input") as file:
    lines = file.readlines()

directories = defaultdict(int)
current_location = Path("/")

for line in lines:
    match line.split():
        case "$", "cd", "/":
            current_location = Path("/")
        case "$", "cd", "..":
            current_location = current_location.parent
        case "$", "cd", goto:
            current_location = current_location / goto
        case size, filename:
            if size.isdigit():  # Ignore directories
                for path in accumulate(current_location.parts):
                    directories[path] += int(size)

print(f"Part 1: {sum(size for size in directories.values() if size <= 100000)}")

used_size = sorted(directories.values())[-1]
print("used size", used_size)
unused_size = 70_000_000 - used_size
print("unused size", unused_size)
for size in sorted(directories.values()):
    if unused_size + size >= 30_000_000:
        print(f"Part 2: {size}")
        break
