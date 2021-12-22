#! /usr/bin/env python3 

def PartOne(lst):
    n = 0
    for x in range(1, len(lst)):
        if lst[x-1] < lst[x]:
            n+=1
    return n

def PartTwo(lst):
    n = 0
    for x in range(3, len(lst)):
        prev = lst[x-3] + lst[x-2] + lst[x-1]
        next = lst[x-2] + lst[x-1] + lst[x]
        if prev < next:
            n +=1
    return n

if __name__ == '__main__':
    file = list(map(int,open('./input.txt', 'r').read().rsplit()))
    print(PartOne(file))
    print(PartTwo(file))

