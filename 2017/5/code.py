# Advent of code Year 2017 Day 5 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [int(number) for number in input_file]

table = input.copy()
i = 0
n = 0
while i < len(table):
    table[i] += 1
    i += table[i] - 1
    n += 1
print("Part One : "+ str(n))

table = input.copy()
i = 0
n = 0
while i < len(table):
    if table[i] >= 3:
        table[i] -= 1
        i += table[i] + 1
    else:
        table[i] += 1
        i += table[i] - 1
    n += 1

print("Part Two : "+ str(n))