#! /usr/bin/env python3

class Table:
    def __init__(self, table):
        self.table = table
        self.last_number = None

    def print(self):
        for row in self.table:
            print(row)

    def check_table(self, number):
        for row_index in range(len(self.table)):
            for col_index in range(len(self.table)):
                if self.table[row_index][col_index] == number:
                    self.table[row_index][col_index] = "x"

    def sum_table_numbers(self):
        sum = 0
        for row in self.table:
            for i in row:
                if not i == "x":
                    sum += i
        return sum

def check_list(number, table) -> list:
    for row_index in range(len(table)):
        for col_index in range(len(table)):
            cell = table[row_index][col_index]
            if cell == number:
                table[row_index][col_index] = "x"

    return table

def check_winner(table) -> bool:
    for row_index in range(len(table)):
        won = True
        for col_index in range(len(table)):
            if not table[row_index][col_index] == "x" :
                won = False
        if won:
            return True

    for row_index in range(len(table)):
        won = True
        for col_index in range(len(table)):
            if not table[col_index][row_index] == "x":
                 won = False
        if won:
            return True
    return False


def split_array(lst, num) -> list:
    tables = []
    for _ in range(len(lst) // num):
        tables.append(lst[:num])
        lst = lst[num:]
    return tables


def PartOne(lst):
    numbers = list(map(int, lst[0].split(",")))
    tables = split_array(list(map(int, lst[1:])), 25)

    for n in range(len(tables)):
        tables[n] = Table(split_array(tables[n], 5))

    for number in numbers:
        for table in tables:
            check_list(number, table.table)
            if check_winner(table.table):
                return table.sum_table_numbers() * number

def PartTwo(lst):
    numbers = list(map(int, lst[0].split(",")))
    tables = split_array(list(map(int, lst[1:])), 25)

    for n in range(len(tables)):
        tables[n] = Table(split_array(tables[n], 5))

    l = []
    for number in numbers:
        for table in tables:
            check_list(number, table.table)
            if check_winner(table.table):
                if table.last_number is None:
                    table.last_number = number
                    l.append(table.sum_table_numbers() * number)

    return l[-1]

if __name__ == '__main__':
    file = open('./input.txt').read().rstrip("\n").split()
    file2 = open('./input2.txt').read().rstrip("\n").split()
    print("Part One:", PartOne(file))
    print("Part Two:", PartTwo(file))
