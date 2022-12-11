# This one really didn't work out, look at try 2 instead
import json
from collections import defaultdict
from pathlib import Path

with open("test_input") as file:
    lines = file.readlines()


def getFromDict(dataDict, mapList):
    if len(mapList) == 1:
        return dataDict[mapList[0]]
    else:
        return getFromDict(dataDict[mapList[0]], mapList[1:])


def setInDict(dataDict, mapList, value):
    if getFromDict(dataDict, mapList[:-1])[mapList[-1]] != {}:
        raise Exception(f"not empty {dataDict}, {mapList}, {getFromDict(dataDict, mapList[:-1])}")
        exit(1)

    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value
    print(dataDict)


dirsums = []


def traverse(data):
    if isinstance(data, int):
        return data

    sum = 0
    for key, value in data.items():
        i = traverse(value)
        print(f"key: {key} i: {i}")
        sum += i
        if isinstance(value, dict) and sum <= 100000:
            print(f"{key}: {value}")
            dirsums.append( sum)
    return sum


current_location = Path("/")
directories = defaultdict(lambda: defaultdict(defaultdict))
for line in lines:
    print(f"input: {line.strip()}, {current_location}")
    if line.startswith("$ cd"):
        goto = line.split("$ cd")[1].strip()
        if goto == "/":
            current_location = Path("/")
        elif goto == "..":
            current_location = current_location.parent
        else:
            current_location = current_location / goto
        print(f"cd {goto}, {current_location}")
        continue
    if not line.startswith("$ "):
        if line.startswith("dir "):
            # continue
            dir_location = current_location / line.split("dir ")[1].strip()
            print(dir_location)
            setInDict(directories, dir_location.parts, defaultdict(defaultdict))
        else:
            size, filename = line.split()
            print(current_location / filename)
            setInDict(directories, (current_location / filename).parts, int(size))
traverse(directories)
print(dirsums)
print(json.dumps(directories, indent=4))
print(sum(dirsums))
