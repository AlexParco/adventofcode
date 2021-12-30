#! /usr/bin/env python3

def PartOne(lst):
    table = [[0 for _ in range(1000)] for _ in range(1000)]

    for n in lst:
        n = n.split(" -> ")
        x1, y1, x2, y2 = map(int, n[0].split(",") + n[1].split(","))
        if x1 == x2 or y1 == y2:
            cord = sorted(((x1,y1), (x2,y2)))
            cord1, cord2 = cord
            for x in range(cord1[0], cord2[0]+1):
                for y in range(cord1[1], cord2[1]+1):
                    table[x][y] +=1

    points = 0
    for row in range(len(table)):
        for col in range(len(table)):
            if table[row][col] > 1:
                points +=1

    return points

def PartTwo(lst):
    table = [[0 for _ in range(1000)] for _ in range(1000)]

    for n in lst:
        n = n.split(" -> ")
        x1, y1, x2, y2 = map(int, n[0].split(",") + n[1].split(","))
        cord = sorted(((x1,y1), (x2,y2)))
        cord1, cord2 = cord
        if cord1[0] == cord2[0] or cord1[1] == cord2[1]:

            for x in range(cord1[0], cord2[0]+1):
                for y in range(cord1[1], cord2[1]+1):
                    table[x][y] +=1
        else:
            slope = (cord2[1] - cord1[1]) / (cord2[0] - cord1[0])
            y = cord1[1]
            for x in range(cord1[0], cord2[0]+1):
                table[x][int(y)] +=1
                y += slope
        
    points = 0
    for row in range(len(table)):
        for col in range(len(table)):
            if table[row][col] > 1:
                points +=1

    return points

if __name__=='__main__':
    file = open('./input.txt', 'r').read().rstrip().split("\n")
    print("Part One:", PartOne(file))
    print("Part Two:", PartTwo(file))

