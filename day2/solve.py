#! /usr/bin/env python3 

# using if
def PartOne(lst):
    horizontal = 0
    depth = 0
    for x in lst:
        x = x.rsplit()
        if len(x) == 2:
            if x[0] == "forward":
                horizontal += int(x[1])
            elif x[0] == "down":
                depth += int(x[1])
            elif x[0] == "up":
                depth -= int(x[1])
    return depth * horizontal 

# using match
def PartTwo(lst):
    horizontal = 0
    aim = 0
    depth = 0
    for x in lst:
        x = x.rsplit()
        if len(x) == 2:
            match x[0]:
                case "down":
                    aim += int(x[1])
                case "up":
                    aim -= int(x[1])
                case "forward":
                    horizontal += int(x[1])
                    depth += aim * int(x[1])
    return depth * horizontal


if __name__ == '__main__':
    file = open('./input.txt').read().split("\n")
    print(PartOne(file))
    print(PartTwo(file))
