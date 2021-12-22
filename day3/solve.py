#! /usr/bin/env python3
def getMaxKey(dict):
    return [key for key, value in dict.items() if value == max(dict.values())][0]

def getMinkey(dict):
    return [key for key, value in dict.items() if value == min(dict.values())][0]

from collections import Counter
def PartOne(lst):
    gamma = ""
    epsilon = ""
    for i in range(len(lst[0])):
        d = Counter()
        for x in lst:
            d[x[i]] +=1
        gamma += getMaxKey(d)
        epsilon += getMinkey(d)
    return int(gamma, 2) * int(epsilon, 2)


def PartTwo(lst):
    lstmax = lst[:]
    lstmin = lst[:]
    n = 0
    while True:
        lstmax = getMaxLstBit(lstmax,n)
        if n == len(lstmax[0])-1:
            break
        n +=1

    n = 0
    while True:
        lstmin = getMinLstBit(lstmin,n)
        if n == len(lstmin[0])-1:
            break
        n +=1

    og = int(lstmax[0], 2)
    co = int(lstmin[0], 2)
    return og * co

def getMaxLstBit(lst, n):
    d = Counter()
    l = []
    for x in lst:
        d[x[n]] +=1
    for x in lst:
        if d['0'] == d['1']:
            if x[n] == '1':
                l.append(x)
        elif x[n] == getMaxKey(d):
            l.append(x)
    return l

def getMinLstBit(lst, n):
    d = Counter()
    l = []
    for x in lst:
        d[x[n]] +=1
    for x in lst:
        if d['0'] == d['1']:
            if x[n] == '0':
                l.append(x)
        elif x[n] == getMinkey(d):
            l.append(x)
    return l

if __name__=='__main__':
    file = open('./input.txt').read().rstrip("\n").split()
    print(PartOne(file))
    print(PartTwo(file))
